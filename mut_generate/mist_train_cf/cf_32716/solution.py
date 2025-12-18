"""
QUESTION:
Implement the `parse_mesh_vectorized_connection` function, which generates a C++ code snippet based on the input connection information and returns the generated code as a string. The function takes in five parameters: `connection`, `nodemap`, `mat_name`, `network_name` (default value is 'network'), and `looped_definition` (default value is False). The generated code snippet should include the declaration of `node_i` and `node_o` as strings representing the indices of the input and output nodes, the declaration of `params_node_i_node_o` as a map of strings to strings, conditional assignment of `i` and `o` based on the value of `looped_definition`, and iteration through the attributes of the `connection` dictionary to populate the `params_node_i_node_o` map.
"""

def parse_mesh_vectorized_connection(connection, nodemap, mat_name, network_name='network', looped_definition=False) -> str:
    node_i = str(nodemap[connection['In']])
    node_o = str(nodemap[connection['Out']])
    s = '\t\t\tstd::map<std::string, std::string> params_' + node_i  + '*' + node_o + ';\n'
    if looped_definition:
        i = str(len(nodemap))+'*i+'+node_i
        o = str(len(nodemap))+'*i+'+node_o
    else:
        i = node_i
        o = node_o
    for ak, av in connection.items():
        s += f'\t\t\tparams_{node_i}*{node_o}["{ak}"] = "{av}";\n'
    return s