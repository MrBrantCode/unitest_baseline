"""
QUESTION:
Implement a function `resource_allocator` that allocates resources to threads based on their scarcity, preventing potential deadlocks in a multithreaded program with five threads (T1, T2, T3, T4, T5) requiring specific resources (R1, R2, R3, R4, R5). The function should prioritize the allocation of resources based on their availability and return the allocation order. Assume the resources have varying levels of availability and are represented by a dictionary where the keys are resource names and the values are their corresponding priorities.
"""

def resource_allocator(resources):
    """
    Allocates resources to threads based on their scarcity, preventing potential deadlocks.
    
    Args:
    resources (dict): A dictionary where the keys are resource names and the values are their corresponding priorities.
    
    Returns:
    list: The allocation order of resources.
    """
    
    # Sort the resources based on their priorities
    sorted_resources = sorted(resources.items(), key=lambda item: item[1])
    
    # Return the allocation order as a list of resource names
    return [resource[0] for resource in sorted_resources]