"""
QUESTION:
Write a function `detect_deadlock(allocated, max_demand, available)` that takes three parameters: `allocated`, a 2D list representing the current allocation of resources to processes; `max_demand`, a 2D list representing the maximum demand of resources by processes; and `available`, a list representing the current available resources of each type. The function should return `True` if the system is in a safe state (i.e., no deadlock), and `False` otherwise. The function should not modify the input lists.
"""

def is_safe(allocated, max_demand, available):
    n = len(allocated)  # Number of processes
    m = len(available)  # Number of resource types

    # Initialize work and finish arrays
    work = available[:]
    finish = [False] * n

    # Find a process that can be executed
    while True:
        found = False
        for i in range(n):
            if not finish[i] and all(need <= work[j] for j, need in enumerate(max_demand[i])):
                # Process can be executed
                found = True
                finish[i] = True
                work = [work[j] + allocated[i][j] for j in range(m)]
                break

        if not found:
            break

    return all(finish)