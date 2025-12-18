"""
QUESTION:
Implement a function called `check_data_locality` that takes a list of nodes and their corresponding data storage locations as input, and returns a dictionary indicating the level of data locality for each node. The levels of data locality should be in descending order of effectiveness: PROCESS_LOCAL, NODE_LOCAL, NO_PREF, RACK_LOCAL, and ANY. The function should also consider the impact of data partitioning and storage methodologies on data locality.

Restrictions: The function should only consider the given list of nodes and data storage locations. It should not rely on any external libraries or Spark configurations.
"""

def check_data_locality(nodes):
    """
    This function takes a list of nodes and their corresponding data storage locations as input, 
    and returns a dictionary indicating the level of data locality for each node.
    
    Parameters:
    nodes (list): A list of tuples containing the node name and its data storage location.
    
    Returns:
    dict: A dictionary with node names as keys and their corresponding data locality levels as values.
    """
    
    # Define the levels of data locality in descending order of effectiveness
    data_locality_levels = ["PROCESS_LOCAL", "NODE_LOCAL", "NO_PREF", "RACK_LOCAL", "ANY"]
    
    # Initialize an empty dictionary to store the data locality levels for each node
    data_locality = {}
    
    # Iterate over each node in the input list
    for node in nodes:
        # Extract the node name and its data storage location
        node_name, storage_location = node
        
        # Determine the data locality level based on the storage location
        if storage_location == "same JVM":
            data_locality[node_name] = data_locality_levels[0]  # PROCESS_LOCAL
        elif storage_location == "same node":
            data_locality[node_name] = data_locality_levels[1]  # NODE_LOCAL
        elif storage_location == "same rack":
            data_locality[node_name] = data_locality_levels[3]  # RACK_LOCAL
        else:
            data_locality[node_name] = data_locality_levels[-1]  # ANY
    
    # Return the dictionary containing the data locality levels for each node
    return data_locality