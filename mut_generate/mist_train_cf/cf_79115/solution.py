"""
QUESTION:
Implement a function named `map_reduce_optimization` that optimizes the MapReduce task by mitigating data skew, a phenomenon that occurs when data is not evenly distributed across reducers.
"""

def map_reduce_optimization(data, num_reducers):
    """
    This function optimizes the MapReduce task by mitigating data skew.
    
    It takes in two parameters: 
    data (list): The input data to be processed.
    num_reducers (int): The number of reducers available.
    
    The function returns a list of lists where each sublist contains the data to be processed by a reducer.
    """
    
    # Calculate the size of each reducer's workload
    workload_size = len(data) // num_reducers
    
    # Initialize the list to store the workload for each reducer
    reducer_workloads = []
    
    # Calculate the start and end indices for each reducer's workload
    for i in range(num_reducers):
        start = i * workload_size
        end = (i + 1) * workload_size if i < num_reducers - 1 else len(data)
        
        # Append the workload for each reducer to the list
        reducer_workloads.append(data[start:end])
    
    return reducer_workloads