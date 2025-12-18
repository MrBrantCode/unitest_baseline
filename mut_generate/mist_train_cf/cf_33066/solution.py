"""
QUESTION:
Implement the `build_sub_graph` method in the `SearchSpaceBuilder` class. The `build_sub_graph` method should take two parameters: `source` and `num_layers`. It should construct a sub-graph with the specified number of layers, starting with the `source` node, and return the constructed sub-graph. The `SearchSpaceBuilder` class has `input_shape` and `output_shape` attributes, but they are not used in this method.
"""

def build_sub_graph(source, num_layers):
    # Initialize the sub-graph with the source node
    sub_graph = [source]

    # Add layers to the sub-graph
    for _ in range(num_layers):
        # Assuming a simple layer representation for demonstration purposes
        layer = "layer"  # Replace with actual layer creation logic
        sub_graph.append(layer)

    return sub_graph