"""
QUESTION:
Write a function `extract_graphics_card_info` that takes a string `nume2` as input, representing the name of a computer graphics card consisting of alphanumeric characters and underscores. The function should return a dictionary containing the extracted brand and model information. The string format is assumed to be in the form of "brand_model_details", where the brand is the first part before the first underscore and the model is the remaining parts joined by underscores.
"""

def extract_graphics_card_info(nume2):
    info = {}
    parts = nume2.split('_')
    if len(parts) >= 2:
        info['brand'] = parts[0]
        info['model'] = '_'.join(parts[1:])
    return info