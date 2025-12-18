"""
QUESTION:
Implement a `node_inflow_results` property in a class that returns a list of dictionaries representing the inflow results for each node in a network. Each dictionary should contain the node name, type, and additional keys based on the flow type ('CFS' or 'GPM'). If the flow type is 'CFS', include 'CFS Inflow' with the inflow value in cubic feet per second; if the flow type is 'GPM', include 'GPM Inflow' with the inflow value in gallons per minute. The class has attributes `ftype` (the flow type) and `nodes` (a list of dictionaries representing the nodes). Each node dictionary should have keys 'name', 'type', and either 'cfs_inflow' or 'gpm_inflow' based on the flow type. The property should handle both 'CFS' and 'GPM' flow types and return the appropriate inflow results for each node.
"""

def node_inflow_results(ftype, nodes):
    inflow_results = []
    for node in nodes:
        result = {'Node': node['name'], 'Type': node['type']}
        if ftype == 'CFS':
            result['CFS Inflow'] = node.get('cfs_inflow', 0)  
        elif ftype == 'GPM':
            result['GPM Inflow'] = node.get('gpm_inflow', 0)  
        inflow_results.append(result)
    return inflow_results