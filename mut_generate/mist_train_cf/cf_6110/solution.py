"""
QUESTION:
Implement a function to calculate the time complexity of the following nested loop structure:

- The outer loop iterates a constant number of times (e.g., 10 times).
- The first inner loop iterates a variable number of times (i) in each iteration of the outer loop.
- The second inner loop also iterates a variable number of times (i) in each iteration of the outer loop.
- The second inner loop has a nested loop that iterates a variable number of times (k) in each iteration of the second inner loop.

The function should return the overall time complexity of the given loop structure in Big O notation.
"""

def calculate_time_complexity(n, i, k):
    """
    Calculate the time complexity of a nested loop structure.

    Args:
        n (int): The constant number of times the outer loop iterates.
        i (int): The variable number of times the first and second inner loops iterate.
        k (int): The variable number of times the nested loop iterates.

    Returns:
        str: The overall time complexity of the given loop structure in Big O notation.
    """

    # Time complexity of the outer loop
    outer_loop_complexity = "O(1)"

    # Time complexity of the first and second inner loops
    inner_loop_complexity = f"2O({i})"

    # Time complexity of the nested loop
    nested_loop_complexity = f"O({k})"

    # Overall time complexity
    overall_complexity = f"{outer_loop_complexity} + {inner_loop_complexity} + {nested_loop_complexity}"

    return overall_complexity

def entance(n, i, k):
    return calculate_time_complexity(n, i, k)