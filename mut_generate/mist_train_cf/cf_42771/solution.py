"""
QUESTION:
Implement the `__get_output_tensors` method of a class to retrieve the output tensors of a subgraph represented as a collection of nodes and edges in a neural network model. The method should take a subgraph as input, iterate through its outputs, and return a dictionary containing the output tensors. If an output is not found in the subgraph, the method should raise an exception.
"""

def get_output_tensors(subgraph):
    output_tensors = OrderedDict()
    model_outputs = subgraph.OutputsAsNumpy()
    for model_output in model_outputs:
        if model_output not in user_shape_dict:
            raise Exception("Please specify all output layers in data_shape.")
        output_tensors[model_output] = model_output_tensor
    return output_tensors