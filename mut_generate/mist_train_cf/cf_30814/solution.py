"""
QUESTION:
You are tasked with optimizing the performance of a data loader. Write a function `optimize_data_loader` that takes an integer `num_classes` as input and returns a dictionary containing the optimized configuration parameters for the data loader, including the batch size, shuffling setting, pin memory option, and the number of worker processes. The function should consider the trade-offs between these configurations to maximize the data loading efficiency.
"""

import math

def optimize_data_loader(num_classes: int) -> dict:
    batch_size = min(1000, math.ceil(num_classes / 2))  
    shuffle = True if num_classes > 100 else False  
    pin_memory = True  
    num_workers = min(10, math.ceil(num_classes / 100))  

    return {
        'batch_size': batch_size,
        'shuffle': shuffle,
        'pin_memory': pin_memory,
        'num_workers': num_workers
    }