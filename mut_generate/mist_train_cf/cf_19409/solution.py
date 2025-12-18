"""
QUESTION:
Implement a function `deadlock_prevention(resource_allocation, available_resources, process_requests)` to determine if a deadlock can occur given a resource allocation state and a set of process requests. The function should return a boolean indicating whether a deadlock is possible and a list of processes involved in the deadlock if it exists. 

The function should take three parameters: 
- `resource_allocation`: A dictionary where keys are process IDs and values are lists of resources currently held by the process.
- `available_resources`: A list of resources that are currently available.
- `process_requests`: A dictionary where keys are process IDs and values are lists of resources requested by the process. 

Restrictions: 
- Assume that there are no other processes in the system apart from those specified in `resource_allocation` and `process_requests`. 
- The system does not support resource preemption, i.e., a process cannot be forcibly removed from a resource.
"""

from collections import defaultdict

def deadlock_prevention(resource_allocation, available_resources, process_requests):
    """
    This function determines if a deadlock can occur given a resource allocation state and a set of process requests.

    Args:
        resource_allocation (dict): A dictionary where keys are process IDs and values are lists of resources currently held by the process.
        available_resources (list): A list of resources that are currently available.
        process_requests (dict): A dictionary where keys are process IDs and values are lists of resources requested by the process.

    Returns:
        tuple: A boolean indicating whether a deadlock is possible and a list of processes involved in the deadlock if it exists.
    """

    # Create a directed graph where an edge from process A to process B means process A is holding a resource requested by process B
    graph = defaultdict(list)
    in_degree = {process: 0 for process in resource_allocation}

    # Populate the graph
    for process, requests in process_requests.items():
        for resource in requests:
            for holder, held_resources in resource_allocation.items():
                if resource in held_resources and holder != process:
                    graph[holder].append(process)
                    in_degree[process] += 1

    # Initialize a queue with processes that have no incoming edges (no other process is holding resources they request)
    queue = [process for process in in_degree if in_degree[process] == 0]

    # Perform topological sorting
    while queue:
        process = queue.pop(0)
        for neighbor in graph[process]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If there are remaining nodes with incoming edges, a cycle exists and a deadlock is possible
    deadlock_processes = [process for process in in_degree if in_degree[process] != 0]
    return len(deadlock_processes) > 0, deadlock_processes