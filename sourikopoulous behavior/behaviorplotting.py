import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

def plot_two_files(filename1, filename2, style_params=None):
    """
    Plot data from two files in a vertically stacked arrangement, with responsive sizing.
    The plots will automatically adjust to window size and share the x-axis label.
    
    Parameters:
    -----------
    filename1 : str
        Path to the first data file
    filename2 : str
        Path to the second data file
    style_params : dict
        Dictionary containing all styling parameters
    """
    
    if style_params is None:
        style_params = {}
    
    try:
        # Set font family for consistent styling across the plots
        plt.rcParams['font.family'] = style_params.get('font_family', 'Arial')
        
        # Create a responsive figure with automatic layout management
        fig = plt.figure(constrained_layout=True)
        
        # Create a 2x1 grid of subplots that will scale with the figure
        gs = fig.add_gridspec(2, 1)
        axes = [fig.add_subplot(gs[i, 0]) for i in range(2)]
        
        # Get colors for the two plots - using the first two colors from our scheme
        colors = style_params.get('colors', plt.cm.Set2([0, 0.2]))[:2]
        
        # Define multi-line y-labels for the two subplots
        ylabels = [
            "Membrane\nVoltage (V)",        # two-line label for top subplot
            "Output Spikes\nVoltage (V)"   # two-line label for bottom subplot
        ]
        
        # Process each file and create its subplot
        for idx, (filename, ax, color) in enumerate(zip([filename1, filename2], axes, colors)):
            # Load and process the data from each file
            raw_data = np.loadtxt(filename, skiprows=1)
            time_ns = raw_data[:, 0] * 1e9  # Convert time to nanoseconds
            voltage = raw_data[:, 2]
            
            # Create the plot with specified styling
            ax.plot(
                time_ns,
                voltage,
                linewidth=style_params.get('line_width', 2),
                marker=style_params.get('marker', ''),
                color=color
            )
            
            # Add grid for better readability
            if style_params.get('grid', True):
                ax.grid(
                    True,
                    linestyle=style_params.get('grid_style', '--'),
                    alpha=style_params.get('grid_alpha', 0.7)
                )
            
            # Configure axis number formatting to avoid scientific notation
            formatter = ScalarFormatter(useOffset=False)
            formatter.set_scientific(False)
            ax.xaxis.set_major_formatter(formatter)
            
            # Style the tick labels with bold font
            ax.tick_params(labelsize=style_params.get('tick_size', 10))
            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontweight('bold')
            
            # Set consistent x-axis limits for both plots
            ax.set_xlim(
                style_params.get('xlim_min', 0),
                style_params.get('xlim_max', 30)
            )
            
            # Handle x-axis labels - only show on the bottom plot
            if idx == 0:  # Top plot
                ax.set_xticklabels([])
                ax.set_xlabel('')
            else:  # Bottom plot
                ax.set_xlabel(
                    style_params.get('xlabel', 'Time (ns)'),
                    fontsize=style_params.get('label_size', 12),
                    fontweight='bold'
                )
            
            # Use multi-line y-axis labels for each subplot
            ax.set_ylabel(
                ylabels[idx],
                fontsize=style_params.get('label_size', 12),
                fontweight='bold'
            )
        
        # Enable automatic resizing for window adjustments
        fig.set_tight_layout(True)
        
        # Save the figure if an output path is specified
        if 'output_path' in style_params:
            plt.savefig(
                style_params['output_path'],
                dpi=style_params.get('dpi', 300),
                bbox_inches='tight'
            )
        
        # Display the plot
        plt.show()
        
    except Exception as e:
        print(f"Error reading or plotting data: {e}")

def main():
    # Define custom colors for visual distinction between plots
    custom_colors = ['#1f77b4', '#ff7f0e']  # Blue and Orange
    
    # Define styling parameters for professional visualization
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
        # Removed 'ylabel' since we have two distinct multi-line labels
        
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

    # Specify the two input files to be plotted
    file1 = 'net3_data.txt'
    file2 = 'net1_data.txt'

    # Generate the plots
    plot_two_files(file1, file2, style_params)

if __name__ == "__main__":
    main()
