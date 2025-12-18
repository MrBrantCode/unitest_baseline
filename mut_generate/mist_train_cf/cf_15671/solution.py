"""
QUESTION:
Given a maximum stack size for a process of 256MB and each thread requiring 1MB of stack space, write a function called `max_threads` to calculate the maximum number of threads that can simultaneously run in a single process.
"""

def max_threads(max_stack_size, thread_stack_size):
    """
    Calculate the maximum number of threads that can run in a process.

    Args:
    max_stack_size (int): The maximum stack size for a process in MB.
    thread_stack_size (int): The stack space required for each thread in MB.

    Returns:
    int: The maximum number of threads that can run in a process.
    """
    return max_stack_size // thread_stack_size

# For this problem, the max_threads function will be used as follows:
# max_threads(256, 1)