"""
QUESTION:
Implement a Python function `first_fit_allocation` that allocates memory blocks to processes based on the First Fit algorithm. The function should take two parameters: `memory_blocks`, a list of integers representing available memory block sizes, and `processes`, a list of integers representing process memory requirements in order of arrival. Return a list of integers representing the memory block index allocated to each process, with -1 indicating no allocation.
"""

def first_fit_allocation(memory_blocks, processes):
    allocation = [-1] * len(processes)  

    for i, process in enumerate(processes):
        for j, block in enumerate(memory_blocks):
            if block >= process:  
                allocation[i] = j  
                memory_blocks[j] -= process  
                break  

    return allocation