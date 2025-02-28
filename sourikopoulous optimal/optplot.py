import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter
from matplotlib.gridspec import GridSpec

def get_si_prefix(value):
    """
    Convert a value to its nearest SI prefix representation.
    This function helps make measurements more readable by using appropriate
    SI prefixes (e.g., converting 0.001V to 1mV).
    
    Parameters:
    -----------
    value : float
        The value to convert
        
    Returns:
    --------
    tuple : (scaled_value, prefix, scale)
        scaled_value: The value scaled to its appropriate SI prefix
        prefix: The SI prefix string
        scale: The scale factor used
    """
    # Define SI prefixes from yotta (10^24) to yocto (10^-24)
    si_prefixes = {
        24: 'Y', 21: 'Z', 18: 'E', 15: 'P', 12: 'T', 9: 'G',
        6: 'M', 3: 'k', 0: '', -3: 'm', -6: 'μ', -9: 'n',
        -12: 'p', -15: 'f', -18: 'a', -21: 'z', -24: 'y'
    }
    
    if value == 0:
        return 0, '', 1
    
    # Calculate appropriate SI prefix exponent
    exponent = int(np.floor(np.log10(abs(value)) / 3) * 3)
    exponent = max(min(exponent, max(si_prefixes.keys())), min(si_prefixes.keys()))
    
    scale = 10 ** exponent
    scaled_value = value / scale
    prefix = si_prefixes[exponent]
    
    return scaled_value, prefix, scale

def analyze_voltage_sweeps(filename, style_params=None):
    """
    Analyze and plot voltage sweep data with customizable styling.
    Creates three plots showing frequency, energy per spike, and optimization score.
    Prints comprehensive analysis including minimum/maximum values and optimal point metrics.
    
    Parameters:
    -----------
    filename : str
        Path to the input data file
    style_params : dict
        Dictionary containing styling parameters for plot customization
    """
    if style_params is None:
        style_params = {}
    
    # Set global font settings
    plt.rcParams['font.family'] = style_params.get('font_family', 'Arial')
    plt.rcParams['font.weight'] = 'bold'
    
    # Read and process the data
    df = pd.read_csv(filename, sep='\s+')
    df = df[df['Energy_Per_Spike'] != 0]  # Filter out zero energy points
    
    # Prepare data for plotting
    x = df['VDD'].values
    x_smooth = np.linspace(x.min(), x.max(), 300)
    
    # Find minimum frequency
    freq_min_idx = np.argmin(df['Frequency'].values)
    freq_min_x = x[freq_min_idx]
    freq_min_y = df['Frequency'].values[freq_min_idx]
    freq_min_val, freq_min_prefix, _ = get_si_prefix(freq_min_y)
    
    # Find maximum energy
    energy_max_idx = np.argmax(df['Energy_Per_Spike'].values)
    energy_max_x = x[energy_max_idx]
    energy_max_y = df['Energy_Per_Spike'].values[energy_max_idx]
    energy_max_val, energy_max_prefix, _ = get_si_prefix(energy_max_y)
    
    # Print minimum frequency and maximum energy information
    print("\nExtreme Values:")
    print(f"Minimum Frequency: {freq_min_val:.3g} {freq_min_prefix}Hz at {freq_min_x:.3f}V")
    print(f"Maximum Energy: {energy_max_val:.3g} {energy_max_prefix}J at {energy_max_x:.3f}V")
    
    # Calculate analysis points for optimal markers
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
    
    # Get metrics at optimal voltage point
    opt_freq = df['Frequency'].values[opt_idx]
    opt_energy = df['Energy_Per_Spike'].values[opt_idx]
    
    # Convert optimal point metrics to SI units
    opt_freq_val, opt_freq_prefix, _ = get_si_prefix(opt_freq)
    opt_energy_val, opt_energy_prefix, _ = get_si_prefix(opt_energy)
    
    # Print metrics at optimal voltage
    print(f"\nMetrics at Optimal Voltage ({opt_voltage:.3f}V):")
    print(f"Frequency: {opt_freq_val:.3g} {opt_freq_prefix}Hz")
    print(f"Energy: {opt_energy_val:.3g} {opt_energy_prefix}J")
    print(f"Optimization Score: {max_score:.3f}")
    
    # Get SI prefix information for scaling
    _, freq_prefix, freq_scale = get_si_prefix(df['Frequency'].max())
    _, energy_prefix, energy_scale = get_si_prefix(df['Energy_Per_Spike'].max())
    
    # Configure the three plots with SI-adjusted labels
    plot_configs = [
        {
            'data': df['Frequency'].values / freq_scale,
            'title': 'Spiking Frequency',
            'ylabel': f'Frequency ({freq_prefix}Hz)',
            'color': style_params.get('line_color1', 'darkblue'),
            'max_x': freq_max_x,
            'max_y': freq_max_y / freq_scale,
            'text': f'Max: {freq_max_x:.3g}V\n{freq_max_y/freq_scale:.3g} {freq_prefix}Hz'
        },
        {
            'data': df['Energy_Per_Spike'].values / energy_scale,
            'title': 'Energy per Spike',
            'ylabel': f'Energy per Spike ({energy_prefix}J)',
            'color': style_params.get('line_color2', 'darkorange'),
            'max_x': energy_min_x,
            'max_y': energy_min_y / energy_scale,
            'text': f'Min: {energy_min_x:.3g}V\n{energy_min_y/energy_scale:.3g} {energy_prefix}J'
        },
        {
            'data': opt_score,
            'title': 'Optimization Score',
            'ylabel': 'Optimization Score',
            'color': style_params.get('line_color3', 'darkgreen'),
            'max_x': opt_voltage,
            'max_y': max_score,
            'text': f'Optimal: {opt_voltage:.3g}V\nScore: {max_score:.3g}'
        }
    ]
    
    # Create figure with three subplots
    fig = plt.figure(figsize=(18, 6), constrained_layout=True)
    gs = GridSpec(1, 3, figure=fig)
    
    def format_tick_value(x, pos):
        """Format tick labels with max 3 significant digits"""
        if x == 0:
            return '0'
        formatted = f'{x:.3g}'
        if '.' in formatted:
            formatted = formatted.rstrip('0').rstrip('.')
        return formatted
    
    # Create each subplot
    for i, config in enumerate(plot_configs):
        ax = fig.add_subplot(gs[i])
        
        # Create smoothed data for plotting
        y = config['data']
        y_smooth = np.interp(x_smooth, x, y)
        
        # Plot the main line
        ax.plot(x_smooth, y_smooth, '-',
               color=config['color'],
               linewidth=style_params.get('line_width', 1.4),
               label='_nolegend_')
        
        # Add optimal point marker
        ax.plot(config['max_x'], config['max_y'], 'o',
               color='#FF00FF',
               markersize=10,
               markeredgecolor='white',
               markeredgewidth=1)
        
        # Set axis limits with padding
        x_range = x.max() - x.min()
        ax.set_xlim(x.min() - x_range * 0.05, x.max() + x_range * 0.05)
        
        # Set y-axis limits
        if i != 2:  # For frequency and energy plots
            y_range = y.max() - y.min()
            ax.set_ylim(y.min() - y_range * 0.1, y.max() + y_range * 0.1)
        else:  # For optimization score plot
            ax.set_ylim(-0.05, 1.1)
        
        # Format axis ticks
        ax.yaxis.set_major_formatter(FuncFormatter(format_tick_value))
        
        # Add title and labels
        ax.set_title(config['title'],
                    fontsize=style_params.get('title_size', 14),
                    fontweight='bold',
                    pad=style_params.get('title_pad', 10))
        
        ax.set_xlabel('Supply Voltage (V)',
                     fontsize=style_params.get('label_size', 12),
                     fontweight='bold')
        
        ax.set_ylabel(config['ylabel'],
                     fontsize=style_params.get('label_size', 12),
                     fontweight='bold')
        
        # Add grid if specified
        if style_params.get('grid', True):
            ax.grid(True,
                   linestyle=style_params.get('grid_style', '--'),
                   alpha=style_params.get('grid_alpha', 0.7))
        
        # Configure tick parameters
        ax.tick_params(labelsize=style_params.get('tick_size', 10))
        
        # Configure x-axis formatting
        x_formatter = ScalarFormatter(useOffset=False)
        x_formatter.set_scientific(False)
        ax.xaxis.set_major_formatter(x_formatter)
        
        # Print plot information
        print(f"\nPlot {i+1} Information:")
        print(config['text'])
    
    # Make layout responsive
    def on_resize(event):
        try:
            plt.tight_layout()
        except:
            pass
    
    fig.canvas.mpl_connect('resize_event', on_resize)
    
    # Save figure if specified
    if 'output_path' in style_params:
        plt.savefig(style_params['output_path'],
                   dpi=style_params.get('dpi', 300),
                   bbox_inches='tight')
    
    plt.show()
    
    # Print comprehensive summary with SI prefixes
    print("\nSummary Statistics:")
    freq_min, freq_min_prefix, _ = get_si_prefix(df['Frequency'].min())
    freq_max, freq_max_prefix, _ = get_si_prefix(df['Frequency'].max())
    energy_min, energy_min_prefix, _ = get_si_prefix(df['Energy_Per_Spike'].min())
    energy_max, energy_max_prefix, _ = get_si_prefix(df['Energy_Per_Spike'].max())
    
    print(f"\nVDD range: {df['VDD'].min():.3f}V to {df['VDD'].max():.3f}V")
    print(f"Frequency range: {freq_min:.2f} {freq_min_prefix}Hz to {freq_max:.2f} {freq_max_prefix}Hz")
    print(f"Energy range: {energy_min:.2f} {energy_min_prefix}J to {energy_max:.2f} {energy_max_prefix}J")
    print(f"\nOptimal voltage point: {opt_voltage:.3f}V")
    print(f"  - Frequency: {opt_freq_val:.3g} {opt_freq_prefix}Hz")
    print(f"  - Energy: {opt_energy_val:.3g} {opt_energy_prefix}J")
    print(f"  - Score: {max_score:.3f}")

def main():
    """
    Main function to run the voltage sweep analysis with customized styling parameters.
    """
    style_params = {
        'font_family': 'Arial',
        'dpi': 175,
        'line_width': 2.4,
        'line_color1': 'darkblue',
        'line_color2': 'darkorange',
        'line_color3': 'darkgreen',
        'title_size': 16,
        'title_pad': 10,
        'label_size': 13,
        'tick_size': 18,
        'grid': True,
        'grid_style': '--',
        'grid_alpha': 0.7,
        'output_path': 'voltage_sweep_analysis.png'
    }
    
    input_file = 'sourikopolousoptimal.txt'
    analyze_voltage_sweeps(input_file, style_params)

if __name__ == "__main__":
    main()