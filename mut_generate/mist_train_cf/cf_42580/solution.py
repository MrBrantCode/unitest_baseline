"""
QUESTION:
Implement the function `populate_batches` that takes the following parameters: `i` (current batch index), `batch_size_eval` (size of each batch for evaluation), `num_valid` (total number of instances in the validation dataset), `mask_length` (length of the mask for the input data), `img_channels` (number of channels in the input images), `H_crop` (height of the cropped input images), `W_crop` (width of the cropped input images), and `input_data` (list of tuples containing input, target, and mask for each instance). The function should return `x_batch` (array to store the input data for the batch), `y_batch` (list to store the target values for the batch), and `mask_batch` (list to store the mask values for the batch). The function should populate `x_batch`, `y_batch`, and `mask_batch` based on the input data and parameters.
"""

import numpy as np

def populate_batches(i, batch_size_eval, num_valid, mask_length, img_channels, H_crop, W_crop, input_data):
    instance_init = i * batch_size_eval
    instance_end = min((i + 1) * batch_size_eval, num_valid)
    instance_num = instance_end - instance_init
    
    y_batch = []  
    mask_batch = []  
    x_batch = np.empty((instance_num, mask_length, img_channels, H_crop, W_crop), dtype=np.float32)  
    
    for j in range(instance_num):
        input_instance, target_instance, mask_instance = input_data[instance_init + j]
        x_batch[j] = input_instance
        y_batch.append(target_instance)
        mask_batch.append(mask_instance)
    
    return x_batch, y_batch, mask_batch