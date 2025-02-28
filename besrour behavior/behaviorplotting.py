import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

def plot_multiple_files(filenames, style_params=None):
    """
    Plot data from multiple files with responsive sizing and streamlined labels.
    The plots will automatically adjust to window size and only show the x-axis
    label on the bottom plot.
    
    Parameters:
    -----------
    filenames : list
        List of paths to the text files containing the data
    style_params : dict
        Dictionary containing all styling parameters
    """
    
    if style_params is None:
        style_params = {}
    
    try:
        # Set font family for consistent styling
        plt.rcParams['font.family'] = style_params.get('font_family', 'Arial')
        
        # Create figure with responsive sizing
        # constrained_layout helps with automatic sizing and spacing
        fig = plt.figure(constrained_layout=True)
        
        # Create a grid of subplots that will scale with the figure
        gs = fig.add_gridspec(len(filenames), 1)
        axes = [fig.add_subplot(gs[i, 0]) for i in range(len(filenames))]
        
        # Configure colors for visual distinction
        colors = style_params.get('colors', plt.cm.Set2(np.linspace(0, 1, len(filenames))))
        
        # Define multi-line y-labels for each subplot
        ylabels = [
            "Incoming Synapse\nVoltage (V)",  # two-line label
            "Membrane\n Voltage (V)",          # single-line label
            "Output Spikes\nVoltage (V)"     # two-line label
        ]
        
        # Process each file and create its corresponding subplot
        for idx, (filename, ax, color) in enumerate(zip(filenames, axes, colors)):
            # Load and process the data
            raw_data = np.loadtxt(filename, skiprows=1)
            time_ns = raw_data[:, 0] * 1e9
            voltage = raw_data[:, 2]
            
            # Create the plot
            ax.plot(
                time_ns,
                voltage,
                linewidth=style_params.get('line_width', 2),
                marker=style_params.get('marker', ''),
                color=color
            )
            
            # Configure grid
            if style_params.get('grid', True):
                ax.grid(
                    True,
                    linestyle=style_params.get('grid_style', '--'),
                    alpha=style_params.get('grid_alpha', 0.7)
                )
            
            # Format axis numbers
            formatter = ScalarFormatter(useOffset=False)
            formatter.set_scientific(False)
            ax.xaxis.set_major_formatter(formatter)
            
            # Style tick labels
            ax.tick_params(labelsize=style_params.get('tick_size', 10))
            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontweight('bold')
            
            # Set axis limits
            ax.set_xlim(
                style_params.get('xlim_min', 0),
                style_params.get('xlim_max', 30)
            )
            
            # Remove x-axis labels for all but the bottom plot
            if idx != len(filenames) - 1:
                ax.set_xticklabels([])
                ax.set_xlabel('')
            else:
                # Add x-axis label only to the bottom plot
                ax.set_xlabel(
                    style_params.get('xlabel', 'Time (ns)'),
                    fontsize=style_params.get('label_size', 12),
                    fontweight='bold'
                )
            
            # Set multi-line y-axis label
            ax.set_ylabel(
                ylabels[idx],
                fontsize=style_params.get('label_size', 12),
                fontweight='bold'
            )
        
        # Enable automatic resizing when the window is adjusted
        fig.set_tight_layout(True)
        
        # Save if output path is provided
        if 'output_path' in style_params:
            plt.savefig(
                style_params['output_path'],
                dpi=style_params.get('dpi', 300),
                bbox_inches='tight'
            )
        
        # Show plot with responsive sizing
        plt.show()
        
    except Exception as e:
        print(f"Error reading or plotting data: {e}")

def main():
    # Define custom colors
    custom_colors = ['#2ca02c', '#1f77b4', '#ff7f0e']  # Green, Blue, Orange
    
    # Define styling parameters
    style_params = {
        # Basic plot parameters
        'font_family': 'Arial',
        'dpi': 175,
        'colors': custom_colors,
        
        # Line styling
        'line_width': 2.5,
        'marker': '',
        
        # Axis labels
        'xlabel': 'Time (ns)',
        'label_size': 14,
        'tick_size': 13,
        
        # Grid styling
        'grid': True,
        'grid_style': '--',
        'grid_alpha': 0.7,
        
        # Axis limits
        'xlim_min': 0,
        'xlim_max': 30,
        
        # Output configuration
        'output_path': 'voltage_plots_combined.png'
    }

    # Define input files
    filenames = [
        'net1_data.txt',
        'net2_data.txt',
        'net4_data.txt'
    ]

    # Generate the plots
    plot_multiple_files(filenames, style_params)

if __name__ == "__main__":
    main()
