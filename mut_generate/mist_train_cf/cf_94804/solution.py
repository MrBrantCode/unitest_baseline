"""
QUESTION:
Design a function `execute_n_times(n, block_of_code)` that takes an integer `n` and a block of code as input, and executes the block of code `n` times without using any built-in Python functions or modules for looping or repeating the execution of code. The block of code can contain any number of statements and can accept any number of arguments, but it should not have any side effects or dependencies on external variables.
"""

def execute_n_times(n, block_of_code):
    if n <= 0:
        return
    block_of_code()
    execute_n_times(n - 1, block_of_code)