"""
QUESTION:
Create a function `normalize(data)` that takes a numpy array `data` and normalizes its values to the range -1 to 1. The normalization should be done in the following manner: 
- values outside the range -0.5 to 0.5 should be clipped to -0.5 or 0.5, 
- then scaled to the range -1 to 1, 
- and finally any remaining values should be rounded to the nearest integer, effectively resulting in values of either -1, 0, or 1.
"""

import numpy as np

def normalize(data):
    normalized_data = np.clip(data, -0.5, 0.5)  
    normalized_data = np.divide(normalized_data, 0.5)  
    normalized_data = np.round(normalized_data)  
    return normalized_data