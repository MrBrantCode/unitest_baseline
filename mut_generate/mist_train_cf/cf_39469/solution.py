"""
QUESTION:
Write a function `parse_layers` that takes a non-empty list of dictionaries, where each dictionary represents a layer in a neural network model with 'tags', 'name', and 'depth' as keys. The function should return a dictionary containing the total number of layers, a list of unique tags, the average depth of the layers, and the name of the layer with the maximum depth.
"""

from typing import List, Dict, Union

def parse_layers(layers: List[Dict[str, Union[str, List[str], int]]]) -> Dict[str, Union[int, List[str], float, str]]:
    total_layers = len(layers)
    
    tags = set()
    total_depth = 0
    max_depth = 0
    max_depth_layer_name = ''
    
    for layer in layers:
        tags.update(layer['tags'])
        total_depth += layer['depth']
        if layer['depth'] > max_depth:
            max_depth = layer['depth']
            max_depth_layer_name = layer['name']
    
    unique_tags = list(tags)
    average_depth = total_depth / total_layers
    
    return {
        'total_layers': total_layers,
        'unique_tags': unique_tags,
        'average_depth': average_depth,
        'max_depth_layer_name': max_depth_layer_name
    }