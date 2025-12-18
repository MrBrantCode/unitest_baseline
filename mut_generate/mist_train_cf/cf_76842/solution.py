"""
QUESTION:
Write a function `optimize_function_calls` to optimize a sequence of function calls by eliminating any redundant calls. The function should take as input a list of function names and a dictionary mapping each function to its input and output. The function should return the optimized list of function calls. The input functions will not have any side effects, so the order of calls can be rearranged if necessary.
"""

def optimize_function_calls(function_calls, functions):
    """
    Optimize a sequence of function calls by eliminating any redundant calls.

    Args:
    function_calls (list): A list of function names.
    functions (dict): A dictionary mapping each function to its input and output.

    Returns:
    list: The optimized list of function calls.
    """
    
    # Create a set to store the results of each function call
    results = set()
    
    # Initialize an empty list to store the optimized function calls
    optimized_calls = []
    
    # Iterate over each function call
    for func in function_calls:
        # If the function's output is not already in the results set
        if functions[func]['output'] not in results:
            # Add the function call to the optimized list
            optimized_calls.append(func)
            # Add the function's output to the results set
            results.add(functions[func]['output'])
    
    return optimized_calls