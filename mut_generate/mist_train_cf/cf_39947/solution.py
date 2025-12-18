"""
QUESTION:
Write a function `calculate_parameters` that takes a dictionary `architecture_config` as input, representing the configuration of a convolutional neural network (CNN). The dictionary has two keys: `input_channels` representing the number of input channels to the network, and `layers`, a list of dictionaries, each describing a convolutional layer. Each layer dictionary contains the keys `in_channels`, `mid_channels`, `out_channels`, `kernel_size`, and `downsample_scales`. Calculate the total number of parameters in the CNN using the formula `params = (in_channels * out_channels * kernel_size^2) + out_channels` for each layer and return the total.
"""

def calculate_parameters(architecture_config):
    total_params = 0
    input_channels = architecture_config['input_channels']
    
    for layer in architecture_config['layers']:
        in_channels = layer['in_channels']
        out_channels = layer['out_channels']
        kernel_size = layer['kernel_size']
        params = (in_channels * out_channels * kernel_size**2) + out_channels
        total_params += params
    
    return total_params