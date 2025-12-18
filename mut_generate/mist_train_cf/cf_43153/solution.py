"""
QUESTION:
Implement a function `extract_layer(model, target_layer)` that takes in a nested dictionary representing a neural network model and a target layer name, and returns the dictionary representing the specified layer if it exists. The target layer name may be a nested layer, represented by a string with '.' as the separator. If the layer is not found, return None.
"""

def extract_layer(model, target_layer):
    layers = target_layer.split('.')
    current = model
    for layer in layers:
        if isinstance(current, dict) and layer in current:
            current = current[layer]
        else:
            return None
    return current