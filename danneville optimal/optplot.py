import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter, MultipleLocator

def get_si_prefix(value):
    """
    Determine the appropriate SI prefix for a given value.
    Returns the scale factor and prefix.
    """
    prefixes = ['y', 'z', 'a', 'f', 'p', 'n', 'µ', 'm', '', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    k = -24  # yocto
    while k <= 24:  # up to yotta
        if abs(value) < 10**(k+3):
            break
        k += 3
    scale = 10**k
    prefix = prefixes[k//3 + 8]  # +8 to center on '' prefix
    return scale, prefix

def analyze_voltage_sweeps(filename, style_params=None):
    """
    Analyze and plot voltage sweep data with customizable styling.
    All plots are now displayed in a single window arranged horizontally.
    """
    if style_params is None:
        style_params = {}
        
    plt.rcParams['font.family'] = style_params.get('font_family', 'Arial')
    plt.rcParams['font.weight'] = 'bold'
    
    # Read and process data
    df = pd.read_csv(filename, sep=r'\s+')
    df = df[df['Energy_Per_Spike'] != 0]
    
    x = df['VDD'].values
    x_smooth = np.linspace(x.min(), x.max(), 300)
    
    # Calculate optimization points
    freq_max_idx = np.argmax(df['Frequency'].values)
    freq_max_x = x[freq_max_idx]
    freq_max_y = df['Frequency'].values[freq_max_idx]
    
    energy_min_idx = np.argmin(df['Energy_Per_Spike'].values)
    energy_min_x = x[energy_min_idx]
    energy_min_y = df['Energy_Per_Spike'].values[energy_min_idx]
    
    # Calculate optimization score
    freq_norm = (df['Frequency'].values - df['Frequency'].min()) / \
               (df['Frequency'].max() - df['Frequency'].min())
    energy_norm = 1 - (df['Energy_Per_Spike'].values - df['Energy_Per_Spike'].min()) / \
                     (df['Energy_Per_Spike'].max() - df['Energy_Per_Spike'].min())
    opt_score = freq_norm * energy_norm
    opt_idx = np.argmax(opt_score)
    opt_voltage = x[opt_idx]
    max_score = opt_score[opt_idx]
    opt_energy = df['Energy_Per_Spike'].values[opt_idx]
    opt_frequency = df['Frequency'].values[opt_idx]
    
    # Create plot configurations for all three plots
    plot_configs = [
        {
            'data': df['Energy_Per_Spike'].values,
            'title': 'Energy per Spike',
            'ylabel': 'Energy per Spike',
            'unit': 'J',
            'color': style_params.get('line_color1', 'darkblue'),
            'max_x': energy_min_x,
            'max_y': energy_min_y,
            'smooth_data': np.interp(x_smooth, x, df['Energy_Per_Spike'].values)
        },
        {
            'data': df['Frequency'].values,
            'title': 'Frequency',
            'ylabel': 'Frequency',
            'unit': 'Hz',
            'color': style_params.get('line_color2', 'darkorange'),
            'max_x': freq_max_x,
            'max_y': freq_max_y,
            'smooth_data': np.interp(x_smooth, x, df['Frequency'].values)
        },
        {
            'data': opt_score,
            'title': 'Optimization Score',
            'ylabel': 'Optimization Score',
            'unit': '',
            'color': style_params.get('line_color3', 'darkgreen'),
            'max_x': opt_voltage,
            'max_y': max_score,
            'smooth_data': np.interp(x_smooth, x, opt_score)
        }
    ]
    
    # Create a single figure with three subplots arranged horizontally
    fig = plt.figure(figsize=(21, 5), dpi=style_params.get('dpi', 175))
    
    # Create a grid of subplots with proper spacing
    gs = fig.add_gridspec(1, 3, hspace=0, wspace=0.3)
    
    # Create axes for each subplot
    axes = [fig.add_subplot(gs[0, i]) for i in range(3)]
    
    # Plot each subplot
    for ax, config in zip(axes, plot_configs):
        y = config['data']
        y_smooth = config['smooth_data']
        
        # Get SI prefix for y-axis if needed
        if config['unit']:
            scale, prefix = get_si_prefix(np.max(np.abs(y)))
            y_scaled = y / scale
            y_smooth_scaled = y_smooth / scale
            ylabel = f"{config['ylabel']} ({prefix}{config['unit']})"
        else:
            scale = 1
            y_scaled = y
            y_smooth_scaled = y_smooth
            ylabel = config['ylabel']
        
        # Plot smoothed line
        ax.plot(x_smooth, y_smooth_scaled, '-',
               color=config['color'],
               linewidth=style_params.get('line_width', 1.4))
        
        # Add optimal point marker in neon purple
        ax.plot(config['max_x'], config['max_y']/scale, 'o',
               color='#FF00FF',
               markersize=style_params.get('marker_size', 8))
        
        # Set axis limits
        x_range = x.max() - x.min()
        ax.set_xlim(x.min() - x_range * 0.05, x.max() + x_range * 0.05)
        
        if config['unit']:
            ax.set_ylim(np.min(y_scaled) * 0.95, np.max(y_scaled) * 1.05)
        else:
            ax.set_ylim(-0.05, 1.05)
        
        # Set labels and title
        ax.set_title(config['title'],
                    fontsize=style_params.get('title_size', 14),
                    fontweight='bold',
                    pad=style_params.get('title_pad', 10))
        
        ax.set_xlabel('Supply Voltage (V)',
                     fontsize=style_params.get('label_size', 12),
                     fontweight='bold')
        
        ax.set_ylabel(ylabel,
                     fontsize=style_params.get('label_size', 12),
                     fontweight='bold')
        
        # Add grid
        if style_params.get('grid', True):
            ax.grid(True,
                   linestyle=style_params.get('grid_style', '--'),
                   alpha=style_params.get('grid_alpha', 0.7))
        
        # Set tick parameters
        ax.tick_params(labelsize=style_params.get('tick_size', 10))
        
        # Configure axes to avoid scientific notation for voltage
        formatter = ScalarFormatter(useOffset=False)
        formatter.set_scientific(False)
        ax.xaxis.set_major_formatter(formatter)
        
        # Set x-axis ticks at 0.2V intervals
        ax.xaxis.set_major_locator(MultipleLocator(0.2))
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    if 'output_path' in style_params:
        plt.savefig(style_params['output_path'],
                   dpi=style_params.get('dpi', 300),
                   bbox_inches='tight')
    
    plt.show()
    
    # Get values at 0.3V through interpolation
    freq_03v = np.interp(0.3, x, df['Frequency'].values)
    energy_03v = np.interp(0.3, x, df['Energy_Per_Spike'].values)
    
    freq_scale_03v, freq_prefix_03v = get_si_prefix(freq_03v)
    energy_scale_03v, energy_prefix_03v = get_si_prefix(energy_03v)
    
    print("\nValues at 0.3V:")
    print(f"  Frequency: {freq_03v/freq_scale_03v:.2f} {freq_prefix_03v}Hz")
    print(f"  Energy: {energy_03v/energy_scale_03v:.2f} {energy_prefix_03v}J")
    
    # Print analysis results with clear formatting
    print("\nAnalysis Results:")
    print("-" * 50)
    print("Maximum Frequency Point:")
    print(f"  Supply Voltage: {freq_max_x:.3f} V")
    freq_scale, freq_prefix = get_si_prefix(freq_max_y)
    print(f"  Frequency: {freq_max_y/freq_scale:.2f} {freq_prefix}Hz")
    
    print("\nMinimum Energy Point:")
    print(f"  Supply Voltage: {energy_min_x:.3f} V")
    energy_scale, energy_prefix = get_si_prefix(energy_min_y)
    print(f"  Energy: {energy_min_y/energy_scale:.2f} {energy_prefix}J")
    
    print("\nOptimal Point (Balanced Score):")
    print(f"  Supply Voltage: {opt_voltage:.3f} V")
    opt_freq_scale, opt_freq_prefix = get_si_prefix(opt_frequency)
    opt_energy_scale, opt_energy_prefix = get_si_prefix(opt_energy)
    print(f"  Frequency: {opt_frequency/opt_freq_scale:.2f} {opt_freq_prefix}Hz")
    print(f"  Energy: {opt_energy/opt_energy_scale:.2f} {opt_energy_prefix}J")
    print(f"  Score: {max_score:.3f}")
    print("-" * 50)

def main():
    """
    Main function to run the voltage sweep analysis with customized styling parameters.
    """
    style_params = {
        'font_family': 'Arial',
        'figsize': (7, 5),
        'dpi': 130,
        'line_width': 2.4,
        'line_color1': 'darkblue',
        'line_color2': 'darkorange',
        'line_color3': 'darkgreen',
        'marker_size': 8,
        'title_size': 14,
        'title_weight': 'bold',
        'title_pad': 10,
        'label_size': 12,
        'label_weight': 'normal',
        'tick_size': 18,
        'annotation_size': 14,
        'grid': True,
        'grid_style': '--',
        'grid_alpha': 0.7,
        'output_path': 'voltage_sweep_analysis.png'
    }
    
    input_file = 'dannevilleoptimal.txt'
    analyze_voltage_sweeps(input_file, style_params)

if __name__ == "__main__":
    main()