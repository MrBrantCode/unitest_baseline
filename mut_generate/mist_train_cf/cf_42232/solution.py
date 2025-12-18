"""
QUESTION:
Implement a function named `hunt_ETH_address` that determines the number of CPU cores to use for a specific task. The function takes an optional parameter `cores` which can be 'all' or an integer. If 'all', the function should use all available cores. If an integer, it should use that specific number of cores if it is within the range of available cores. Otherwise, it should default to using 1 core.
"""

from multiprocessing import cpu_count

def hunt_ETH_address(cores='all'):
    available_cores = cpu_count()

    if cores == 'all':
        cores = available_cores
    elif 0 < int(cores) <= available_cores:
        cores = int(cores)
    else:
        cores = 1

    return cores