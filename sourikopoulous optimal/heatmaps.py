import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from matplotlib.gridspec import GridSpec

def get_si_prefix_for_range(data):
    """
    Determines the most appropriate SI prefix for a range of values.
    
    This function analyzes a dataset and finds the most suitable SI prefix by looking
    at the mean order of magnitude of the data. For example, if most values are around
    0.001, it will suggest using milli (m) as the prefix.
    
    Parameters:
    -----------
    data : numpy.ndarray
        Array of values to analyze
        
    Returns:
    --------
    tuple : (scale_factor, prefix)
        scale_factor : float
            The multiplication factor to convert to the chosen SI prefix
        prefix : str
            The SI prefix symbol (e.g., 'μ' for micro, 'm' for milli)
    """
    non_nan = data[~np.isnan(data)]
    if len(non_nan) == 0:
        return 1, ''
    
    mean_abs = np.mean(np.abs(non_nan))
    if mean_abs == 0:
        return 1, ''
    
    exponent = int(np.floor(np.log10(mean_abs)))
    si_exponent = int(np.floor(exponent / 3) * 3)
    
    si_prefixes = {
        24: 'Y', 21: 'Z', 18: 'E', 15: 'P', 12: 'T', 9: 'G',
        6: 'M', 3: 'k', 0: '', -3: 'm', -6: 'μ', -9: 'n',
        -12: 'p', -15: 'f', -18: 'a', -21: 'z', -24: 'y'
    }
    
    si_exponent = max(min(si_exponent, max(si_prefixes.keys())), min(si_prefixes.keys()))
    
    return 10 ** si_exponent, si_prefixes[si_exponent]

def load_and_process_data(data_file):
    """
    Load and process the input data file, converting capacitor values to femtofarads.
    
    Parameters:
    -----------
    data_file : str
        Path to the input data file containing capacitor sweep data
    
    Returns:
    --------
    tuple : (frequency_pivot, energy_pivot)
        Two pivot tables containing the processed frequency and energy data
    """
    df = pd.read_csv(data_file, sep=r'\s+')
    df = df[df['Energy_Per_Spike'] != 0]
    df['Cap1_fF'] = df['Cap1'] * 1e15
    df['Cap2_fF'] = df['Cap2'] * 1e15
    
    frequency_pivot = df.pivot_table(values='Frequency', index='Cap1_fF', columns='Cap2_fF')
    energy_pivot = df.pivot_table(values='Energy_Per_Spike', index='Cap1_fF', columns='Cap2_fF')
    
    return frequency_pivot, energy_pivot

def normalize_data(data):
    """
    Normalize data to range [0, 1] while properly handling NaN values.
    """
    min_val = np.nanmin(data)
    max_val = np.nanmax(data)
    return (data - min_val) / (max_val - min_val)

def interpolate_data(pivot_table, num_points=100):
    """
    Create smooth interpolated data for heatmap visualization.
    """
    x = pivot_table.columns
    y = pivot_table.index
    X, Y = np.meshgrid(x, y)
    Z = pivot_table.values
    
    xi = np.linspace(X.min(), X.max(), num_points)
    yi = np.linspace(Y.min(), Y.max(), num_points)
    xi, yi = np.meshgrid(xi, yi)
    
    zi = griddata((X.flatten(), Y.flatten()), Z.flatten(), (xi, yi), method='linear')
    
    return xi, yi, zi

def create_combined_heatmaps(frequency_pivot, energy_pivot, style_params=None):
    """
    Create three heatmaps showing energy, frequency, and optimization score.
    Also prints minimum frequency and maximum energy values.
    """
    if style_params is None:
        style_params = {}
    
    plt.rcParams['font.family'] = style_params.get('font_family', 'Arial')
    plt.rcParams['font.weight'] = 'bold'
    
    fig = plt.figure(figsize=(18, 6), constrained_layout=True)
    gs = GridSpec(1, 3, figure=fig)
    
    x_freq, y_freq, z_freq = interpolate_data(frequency_pivot, 
                                              num_points=style_params.get('interpolation_points', 100))
    x_energy, y_energy, z_energy = interpolate_data(energy_pivot, 
                                                    num_points=style_params.get('interpolation_points', 100))
    
    z_freq_norm = normalize_data(z_freq)
    z_energy_norm = 1 - normalize_data(z_energy)
    z_combined = z_freq_norm * z_energy_norm
    
    min_freq_idx = np.unravel_index(np.nanargmin(z_freq), z_freq.shape)
    min_freq = z_freq[min_freq_idx]
    min_freq_x = x_freq[min_freq_idx[0], min_freq_idx[1]]
    min_freq_y = y_freq[min_freq_idx[0], min_freq_idx[1]]
    print("\nMinimum Frequency Values:")
    print(f"Frequency: {min_freq:.3e} Hz")
    print(f"Reset Capacitor: {min_freq_x:.2f} fF")
    print(f"Membrane Capacitor: {min_freq_y:.2f} fF")
    
    max_energy_idx = np.unravel_index(np.nanargmax(z_energy), z_energy.shape)
    max_energy = z_energy[max_energy_idx]
    max_energy_x = x_energy[max_energy_idx[0], max_energy_idx[1]]
    max_energy_y = y_energy[max_energy_idx[0], max_energy_idx[1]]
    print("\nMaximum Energy Values:")
    print(f"Energy: {max_energy:.3e} J")
    print(f"Reset Capacitor: {max_energy_x:.2f} fF")
    print(f"Membrane Capacitor: {max_energy_y:.2f} fF")
    
    plot_configs = [
        {
            'data': z_energy,
            'x': x_energy,
            'y': y_energy,
            'title': 'Energy per Spike',
            'base_unit': 'J',
            'cmap': 'RdYlGn_r',
            'subplot': gs[0],
            'optimal_func': np.nanargmin
        },
        {
            'data': z_freq,
            'x': x_freq,
            'y': y_freq,
            'title': 'Spiking Frequency',
            'base_unit': 'Hz',
            'cmap': 'RdYlGn',
            'subplot': gs[1],
            'optimal_func': np.nanargmax
        },
        {
            'data': z_combined,
            'x': x_freq,
            'y': y_freq,
            'title': 'Optimization Score',
            'base_unit': '',
            'cmap': 'RdYlGn',
            'subplot': gs[2],
            'optimal_func': np.nanargmax
        }
    ]
    
    for i, config in enumerate(plot_configs):
        ax = fig.add_subplot(config['subplot'])
        
        if config['base_unit']:
            scale_factor, prefix = get_si_prefix_for_range(config['data'])
            plot_data = config['data'] / scale_factor
        else:
            scale_factor, prefix = 1, ''
            plot_data = config['data']
        
        im = ax.pcolormesh(config['x'], config['y'], plot_data,
                           cmap=config['cmap'],
                           shading=style_params.get('shading', 'auto'))
        
        opt_idx = np.unravel_index(config['optimal_func'](config['data']), config['data'].shape)
        opt_x = config['x'][opt_idx[0], opt_idx[1]]
        opt_y = config['y'][opt_idx[0], opt_idx[1]]
        
        marker_size = style_params.get('optimal_point_size', 10)
        ax.plot(opt_x, opt_y, 'o', color='#FF00FF',
                markersize=marker_size,
                markeredgecolor='white',
                markeredgewidth=marker_size/10)
        
        ax.set_title(config['title'],
                     fontsize=style_params.get('title_size', 14),
                     pad=style_params.get('title_pad', 10),
                     weight='bold')
        ax.set_xlabel(style_params.get('xlabel', 'Reset Capacitor (fF)'),
                      fontsize=style_params.get('label_size', 12),
                      weight='bold')
        if i == 0:
            ax.set_ylabel(style_params.get('ylabel', 'Membrane Capacitor (fF)'),
                          fontsize=style_params.get('label_size', 12),
                          weight='bold')
        
        cbar = fig.colorbar(im, ax=ax)
        if config['base_unit']:
            cbar.ax.set_title(f'{prefix}{config["base_unit"]}',
                              size=style_params.get('colorbar_label_size', 14),
                              pad=10,
                              weight='bold')
        
        ax.tick_params(labelsize=style_params.get('tick_size', 10))
        cbar.ax.tick_params(labelsize=style_params.get('tick_size', 10))
        
        # --- Set both axes to log scale with logarithmically spaced tick positions ---
        ax.set_xscale('log')
        ax.set_yscale('log')
        
        def format_tick(val):
            return f"{val:.0f}" if val >= 1 else f"{val:.1f}"
        
        xticks = np.logspace(np.log10(config['x'].min()), np.log10(config['x'].max()), num=7)
        yticks = np.logspace(np.log10(config['y'].min()), np.log10(config['y'].max()), num=7)
        ax.set_xticks(xticks)
        ax.set_xticklabels([format_tick(x) for x in xticks])
        ax.set_yticks(yticks)
        ax.set_yticklabels([format_tick(y) for y in yticks])
        # -----------------------------------------------------------
        
        if config['base_unit']:
            print(f"\n{config['title']} Optimal Point:")
            print(f"Value: {config['data'][opt_idx]/scale_factor:.3g} {prefix}{config['base_unit']}")
        else:
            print(f"\n{config['title']} Optimal Point:")
            print(f"Score: {config['data'][opt_idx]:.3g}")
        print(f"Membrane Capacitor: {opt_y:.2f} fF")
        print(f"Reset Capacitor: {opt_x:.2f} fF")
    
    def on_resize(event):
        try:
            plt.tight_layout()
        except:
            pass
    
    fig.canvas.mpl_connect('resize_event', on_resize)
    plt.show()

def main():
    """
    Main function to run the analysis with customized styling parameters.
    """
    style_params = {
        'font_family': 'Arial',
        'dpi': 155,
        'interpolation_points': 1000,
        'title_size': 16,
        'label_size': 16,
        'tick_size': 16,
        'colorbar_label_size': 16,
        'title_pad': 15,
        'shading': 'auto',
        'xlabel': 'Reset Capacitor (fF)',
        'ylabel': 'Membrane Capacitor (fF)',
        'optimal_point_size': 14
    }
    
    input_file = 'sourikopolousneuron.txt'
    frequency_pivot, energy_pivot = load_and_process_data(input_file)
    create_combined_heatmaps(frequency_pivot, energy_pivot, style_params)

if __name__ == "__main__":
    main()
