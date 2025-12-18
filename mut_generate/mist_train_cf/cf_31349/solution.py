"""
QUESTION:
Implement a function `extract_layer_info` that takes a `node.pb` object as input and returns a dictionary containing the extracted layer information, including the layer type, input shape, output shape, and any other relevant details available in the `node.pb` object. The function should assume that the `node.pb` object contains all the necessary information about the layer.
"""

def extract_layer_info(node_pb) -> dict:
    layer_info = {}
    layer_info['layer_type'] = node_pb.layer_type
    layer_info['input_shape'] = node_pb.input_shape
    layer_info['output_shape'] = node_pb.output_shape
    # layer_info['other_details'] = node_pb.other_details
    return layer_info