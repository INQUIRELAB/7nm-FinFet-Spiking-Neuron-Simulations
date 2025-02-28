import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def read_power_data(filename):
    vdd = []
    power = []
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            v, p = line.strip().split()
            vdd.append(float(v))
            power.append(float(p))
    return np.array(vdd), np.array(power)

def plot_static_power(file_paths, output_path='static_power_comparison.png', style_params=None):
    # Default style parameters with extensive customization options
    # Add small buffer (percentage) to axis limits
    axis_buffer_percent = 0.05  # 5% buffer
    default_params = {
        # Font settings
        'font_family': 'Arial',
        'font_weight': 'bold',
        
        # Line settings
        'line_width': 2.6,
        'line_styles': ['-', '-', '-'],  # Line style for each dataset
        'colors': ['#1f77b4', '#ff7f0e', '#2ca02c'],  # Colors for each line
        
        # Axis settings
        'label_size': 17,
        'label_weight': 'bold',
        'x_label': 'Supply Voltage (V)',
        'y_label': 'Static Power (W)',
        
        # Title settings
        'title': 'Static Power Comparison of Neuron Models',
        'title_size': 17,
        'title_weight': 'bold',
        'title_pad': 15,
        
        # Legend settings
        'legend_size': 17,
        'legend_weight': 'bold',
        'legend_location': 'best',
        'legend_labels': ['SML', 'DAH', 'BLIF'],
        
        # Tick settings
        'tick_size': 18,
        'tick_weight': 'bold',
        'x_ticks': None,  # Auto by default
        'y_ticks': None,  # Auto by default
        
        # Grid settings
        'grid_major_alpha': 0.2,
        'grid_minor_alpha': 0.2,
        'grid_major_style': '-',
        'grid_minor_style': ':',
        
        # Figure settings
        'figure_size': (10, 6),
        'dpi': 300,
        
        # Plot scale settings
        'x_scale': 'linear',
        'y_scale': 'log'
    }
    
    # Update default parameters with provided ones
    if style_params is not None:
        default_params.update(style_params)
    
    # Validate input files
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} not found")
            return False

    try:
        # Read data
        datasets = [read_power_data(file_path) for file_path in file_paths]
        
        # Create figure
        plt.figure(figsize=default_params['figure_size'])
        
        # Set font family and weight globally
        plt.rcParams['font.family'] = default_params['font_family']
        plt.rcParams['font.weight'] = default_params['font_weight']
        
        # Plot each dataset
        for i, (vdd, power) in enumerate(datasets):
            plt.plot(vdd, power, 
                    default_params['line_styles'][i],
                    label=default_params['legend_labels'][i],
                    linewidth=default_params['line_width'],
                    color=default_params['colors'][i])
        
        # Set scales
        plt.xscale(default_params['x_scale'])
        plt.yscale(default_params['y_scale'])
        
        # Configure grid
        plt.grid(True, which="major", ls=default_params['grid_major_style'], 
                alpha=default_params['grid_major_alpha'])
        plt.grid(True, which="minor", ls=default_params['grid_minor_style'], 
                alpha=default_params['grid_minor_alpha'])
        
        # Set labels
        plt.xlabel(default_params['x_label'], 
                  fontsize=default_params['label_size'],
                  fontweight=default_params['label_weight'])
        plt.ylabel(default_params['y_label'], 
                  fontsize=default_params['label_size'],
                  fontweight=default_params['label_weight'])
        
        # Set title
        plt.title(default_params['title'], 
                 fontsize=default_params['title_size'],
                 fontweight=default_params['title_weight'],
                 pad=default_params['title_pad'])
        
        # Configure legend with bold text using a custom prop dictionary
        legend = plt.legend(fontsize=default_params['legend_size'],
                          loc=default_params['legend_location'])
        plt.setp(legend.get_texts(), weight=default_params['legend_weight'])
        
        # Configure ticks
        plt.xticks(default_params['x_ticks'] if default_params['x_ticks'] is not None else plt.xticks()[0],
                  fontsize=default_params['tick_size'],
                  weight=default_params['tick_weight'])
        plt.yticks(default_params['y_ticks'] if default_params['y_ticks'] is not None else plt.yticks()[0],
                  fontsize=default_params['tick_size'],
                  weight=default_params['tick_weight'])
        
        # Adjust layout and save
        # Get data bounds for all datasets
        all_x = np.concatenate([data[0] for data in datasets])
        all_y = np.concatenate([data[1] for data in datasets])
        
        # Calculate axis limits with buffer
        x_min, x_max = np.min(all_x), np.max(all_x)
        y_max = np.max(all_y)
        
        # Add percentage buffer to limits
        x_buffer = (x_max - x_min) * axis_buffer_percent
        y_buffer = y_max * axis_buffer_percent
        
        plt.xlim(x_min - x_buffer, x_max + x_buffer)
        plt.ylim(2e-10, y_max + y_buffer)  # Fixed minimum y value

        plt.tight_layout()
        plt.savefig(output_path, dpi=default_params['dpi'], bbox_inches='tight')
        plt.show()
        return True

    except Exception as e:
        print(f"Error occurred while plotting: {str(e)}")
        return False

def main():
    default_files = [
        'sourikopolousneuron.txt',
        'dannevilleneuron.txt',
        'besrourneuron.txt'    # Files order matches legend labels order
    ]

    # Font sizes for all text elements
    font_sizes = {
        'label_size': 17,    # Axis labels
        'title_size': 17,    # Plot title
        'legend_size': 17,   # Legend text
        'tick_size': 18,     # Tick labels
    }

    # Example of custom style parameters
    style_params = {
        'line_width': 3.0,
        'colors': ['#ff0000', '#00ff00', '#0000ff'],  # Red, Green, Blue
        'title': 'Static Power Comparison of Neuron Designs',
        'legend_location': 'upper left',
        'grid_major_alpha': 0.3,
        'figure_size': (8, 6),
        'dpi': 175,
        # Add font sizes to style parameters
        **font_sizes
    }

    if len(sys.argv) > 1:
        if len(sys.argv) != 4:
            print("Usage: python plot_static_power.py [sourikopoulos_file danneville_file besour_file]")
            sys.exit(1)
        input_files = sys.argv[1:4]
    else:
        input_files = default_files

    output_path = 'static_power_comparison.png'

    success = plot_static_power(input_files, output_path, style_params)
    
    if success:
        print(f"Plot successfully saved to {output_path}")
    else:
        print("Failed to create plot")
        sys.exit(1)

if __name__ == "__main__":
    main()