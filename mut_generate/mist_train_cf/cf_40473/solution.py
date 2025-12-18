"""
QUESTION:
Implement the function `process_graph` that takes a list of input nodes `f_inputs` and returns two dictionaries, `node` and `edge`. The `node` dictionary should map unique node identifiers to lists containing the node's name, input shapes, and output shapes. The `edge` dictionary should map the unique identifiers of the creators of the input nodes to the unique identifiers of the nodes they create. Each input node in `f_inputs` has `name`, `input_shapes`, `output_shapes`, and `creator` attributes. The function should return the populated `node` and `edge` dictionaries.
"""

def process_graph(f_inputs):
    node = {}
    edge = {}
    for i, input_ in enumerate(f_inputs, start=1):
        node[i] = [input_.name, input_.input_shapes, input_.output_shapes]
    
    creator_ids = [id(input_.creator) for input_ in f_inputs]
    for creator_id, node_id in zip(creator_ids, node.keys()):
        edge[creator_id] = node_id
    
    return node, edge