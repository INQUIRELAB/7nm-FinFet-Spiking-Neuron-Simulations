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

def analyze_cap_sweep(filename, style_params=None):
    """
    Analyze and plot capacitor sweep data with customizable styling.
    All text elements are now set to bold for improved visibility.
    Creates a single figure with three horizontally arranged plots.
    """
    if style_params is None:
        style_params = {}
        
    # Set global font family and weight
    plt.rcParams['font.family'] = style_params.get('font_family', 'Arial')
    plt.rcParams['font.weight'] = 'bold'  # Make all text bold by default
    
    # Read and process data
    df = pd.read_csv(filename, sep=r'\s+')
    df = df[df['Energy_Per_Spike'] != 0]
    df['Cap_fF'] = pd.to_numeric(df['Cap']) * 1e15
    
    avg_data = df.groupby('Cap_fF').agg({
        'Frequency': 'mean',
        'Energy_Per_Spike': 'mean'
    }).reset_index()
    
    avg_data = avg_data.sort_values('Cap_fF')
    
    # Calculate maximum/minimum points
    freq_max_idx = np.argmax(avg_data['Frequency'].values)
    freq_max_x = avg_data['Cap_fF'].values[freq_max_idx]
    freq_max_y = avg_data['Frequency'].values[freq_max_idx]
    
    energy_min_idx = np.argmin(avg_data['Energy_Per_Spike'].values)
    energy_min_x = avg_data['Cap_fF'].values[energy_min_idx]
    energy_min_y = avg_data['Energy_Per_Spike'].values[energy_min_idx]
    
    x = avg_data['Cap_fF'].values
    x_smooth = np.linspace(x.min(), x.max(), 300)
    
    # Calculate optimization score
    freq_norm = (avg_data['Frequency'].values - avg_data['Frequency'].min()) / \
               (avg_data['Frequency'].max() - avg_data['Frequency'].min())
    energy_norm = 1 - (avg_data['Energy_Per_Spike'].values - avg_data['Energy_Per_Spike'].min()) / \
                     (avg_data['Energy_Per_Spike'].max() - avg_data['Energy_Per_Spike'].min())
    opt_score = freq_norm * energy_norm
    
    # Find optimal point
    opt_idx = np.argmax(opt_score)
    opt_cap = x[opt_idx]
    max_score = opt_score[opt_idx]
    
    # Create plot configurations for all three plots with updated titles
    plot_configs = [
        {
            'data': avg_data['Energy_Per_Spike'].values,
            'title': 'Average Energy per Spike',  # Removed "vs Reset Capacitor"
            'ylabel': 'Energy per Spike',
            'unit': 'J',
            'color': style_params.get('line_color1', 'darkblue'),
            'max_x': energy_min_x,
            'max_y': energy_min_y,
            'smooth_data': np.interp(x_smooth, x, avg_data['Energy_Per_Spike'].values)
        },
        {
            'data': avg_data['Frequency'].values,
            'title': 'Average Frequency',  # Removed "vs Reset Capacitor"
            'ylabel': 'Frequency',
            'unit': 'Hz',
            'color': style_params.get('line_color2', 'darkorange'),
            'max_x': freq_max_x,
            'max_y': freq_max_y,
            'smooth_data': np.interp(x_smooth, x, avg_data['Frequency'].values)
        },
        {
            'data': opt_score,
            'title': 'Optimization Score',  # Removed "vs Reset Capacitor"
            'ylabel': 'Optimization Score',
            'unit': '',
            'color': style_params.get('line_color3', 'darkgreen'),
            'max_x': opt_cap,
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
        
        # Add only the optimal point marker in neon purple with larger size
        ax.plot(config['max_x'], config['max_y']/scale, 'o',
               color='#FF00FF',
               markersize=style_params.get('marker_size', 8))
        
        # Set axis limits and ticks
        ax.set_xlim(x.min(), x.max())
        ax.xaxis.set_major_locator(plt.MultipleLocator(1))  # Set step size to 1
        if config['unit']:
            ax.set_ylim(np.min(y_scaled) * 0.95, np.max(y_scaled) * 1.05)
        else:
            ax.set_ylim(0, 1.05)
        
        # Set labels and title with bold weight
        ax.set_title(config['title'],
                    fontsize=style_params.get('title_size', 14),
                    fontweight='bold',
                    pad=style_params.get('title_pad', 10))
        
        ax.set_xlabel('Reset Capacitor (fF)',
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
        
        # Set tick parameters and make tick labels bold
        ax.tick_params(labelsize=style_params.get('tick_size', 10))
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontweight('bold')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    if 'output_path' in style_params:
        plt.savefig(style_params['output_path'],
                   dpi=style_params.get('dpi', 300),
                   bbox_inches='tight')
    
    plt.show()
    
    # Print optimization results with clear formatting
    print("\nAnalysis Results:")
    print("-" * 50)
    print("Maximum Frequency Point:")
    print(f"  Capacitor: {freq_max_x:.2f} fF")
    freq_scale, freq_prefix = get_si_prefix(freq_max_y)
    print(f"  Frequency: {freq_max_y/freq_scale:.2f} {freq_prefix}Hz")
    print("\nMinimum Energy Point:")
    print(f"  Capacitor: {energy_min_x:.2f} fF")
    energy_scale, energy_prefix = get_si_prefix(energy_min_y)
    print(f"  Energy: {energy_min_y/energy_scale:.2f} {energy_prefix}J")
    print("\nOptimal Point (Balanced Score):")
    print(f"  Capacitor: {opt_cap:.2f} fF")
    opt_freq = avg_data['Frequency'].values[opt_idx]
    opt_energy = avg_data['Energy_Per_Spike'].values[opt_idx]
    opt_freq_scale, opt_freq_prefix = get_si_prefix(opt_freq)
    opt_energy_scale, opt_energy_prefix = get_si_prefix(opt_energy)
    print(f"  Frequency: {opt_freq/opt_freq_scale:.2f} {opt_freq_prefix}Hz")
    print(f"  Energy: {opt_energy/opt_energy_scale:.2f} {opt_energy_prefix}J")
    print(f"  Score: {max_score:.3f}")
    print("-" * 50)

def main():
    # Define styling parameters with bold text settings
    style_params = {
        'font_family': 'Arial',
        'figsize': (7, 5),
        'dpi': 130,
        'line_width': 2.4,
        'line_color1': 'darkblue',
        'line_color2': 'darkorange',
        'line_color3': 'darkgreen',
        'marker_size': 11,
        'title_size': 15,
        'title_weight': 'bold',
        'title_pad': 10,
        'label_size': 12,
        'label_weight': 'bold',  # Changed to bold
        'tick_size': 18,
        'annotation_size': 14,
        'grid': True,
        'grid_style': '--',
        'grid_alpha': 0.7,
        'output_path': 'cap_sweep_analysis.png'
    }
    
    input_file = 'dannevilleneuron.txt'
    analyze_cap_sweep(input_file, style_params)

if __name__ == "__main__":
    main()