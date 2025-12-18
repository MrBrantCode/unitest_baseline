"""
QUESTION:
Implement a function `avoid_deadlock` that prevents deadlock by avoiding circular wait when multiple threads are competing for resources. The function should take as input a list of threads and a list of resources, and return True if the system is deadlock-free and False otherwise. Assume that each thread is waiting for a resource and each resource is held by at most one thread.
"""

from collections import defaultdict

def avoid_deadlock(threads, resources):
    """
    This function prevents deadlock by avoiding circular wait when multiple threads are competing for resources.
    
    Args:
        threads (list): A list of threads where each thread is represented as a pair (thread_id, resource_id)
        resources (list): A list of resources where each resource is represented as a pair (resource_id, held_by)
        
    Returns:
        bool: True if the system is deadlock-free, False otherwise
    """
    
    # Create a graph to store the wait relationships between threads
    graph = defaultdict(list)
    
    # Create a dictionary to store the in-degree of each node (thread)
    in_degree = defaultdict(int)
    
    # Populate the graph and in-degree dictionary
    for thread_id, resource_id in threads:
        # Find the thread that holds the resource
        for resource in resources:
            if resource[0] == resource_id:
                held_by = resource[1]
                if held_by is not None:
                    # Add an edge from the current thread to the thread that holds the resource
                    graph[held_by].append(thread_id)
                    # Increment the in-degree of the current thread
                    in_degree[thread_id] += 1
    
    # Initialize a queue with threads that have an in-degree of 0
    queue = [thread_id for thread_id, _ in threads if in_degree[thread_id] == 0]
    
    # Perform topological sorting
    while queue:
        thread_id = queue.pop(0)
        for neighbor in graph[thread_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If there are threads remaining in the in-degree dictionary, then a cycle exists and the system is not deadlock-free
    return len(in_degree) == 0