"""
QUESTION:
Write a function to determine whether a deadlock is possible in a given resource allocation system. The function should take two inputs: `available_resources` (a list of available resources) and `processes` (a list of processes where each process is represented as a list of resources it is holding and resources it is waiting for). The function should return True if a deadlock is possible, False otherwise.
"""

def is_deadlock_possible(available_resources, processes):
    # Create a graph where each node is a process and there is a directed edge from process A to process B if A is waiting for a resource held by B
    graph = [[] for _ in range(len(processes))]
    in_degree = [0] * len(processes)
    
    for i in range(len(processes)):
        for j in range(len(processes)):
            if i != j:
                # Check if process i is waiting for a resource held by process j
                for resource in processes[i][1]:
                    if resource in processes[j][0]:
                        graph[i].append(j)
                        in_degree[j] += 1
    
    # Initialize a queue with all processes that are not waiting for any resources
    queue = [i for i in range(len(processes)) if in_degree[i] == 0]
    
    # Perform topological sorting
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If there are remaining nodes with in-degree greater than 0, then a cycle exists and deadlock is possible
    return any(in_degree)