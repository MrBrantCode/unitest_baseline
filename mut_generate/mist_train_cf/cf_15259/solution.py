"""
QUESTION:
Implement a function `calculate_big_o` that takes three parameters: `recursive_time_complexity` (a string representing the time complexity of the recursive part of an algorithm), `iterative_time_complexity` (a string representing the time complexity of the iterative part of the algorithm), and `recursive_calls` (an integer representing the number of times the recursive part is called from the iterative part). The function should return a string representing the overall time complexity of the algorithm, combining the recursive and iterative parts. Assume the input time complexities are already simplified expressions.
"""

def calculate_big_o(recursive_time_complexity, iterative_time_complexity, recursive_calls):
    if recursive_calls == 0:
        return iterative_time_complexity
    return f"O({recursive_calls} * {iterative_time_complexity})" if recursive_time_complexity == "1" else f"O({recursive_time_complexity} + {recursive_calls} * {iterative_time_complexity})"