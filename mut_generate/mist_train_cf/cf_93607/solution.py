"""
QUESTION:
Write a function `calculate_big_o` that calculates the Big O notation for a given algorithm's time complexity, considering both recursive and iterative approaches. The function should take three parameters: `recursive_time_complexity` (a string representing the time complexity of the recursive part), `iterative_time_complexity` (a string representing the time complexity of the iterative part), and `recursive_calls` (an integer representing the number of recursive calls made by the iterative part). The function should return a string representation of the overall time complexity, assuming the recursive and iterative parts are independent, unless the recursive part is called inside the iterative part, in which case the time complexity of the iterative part should be multiplied by the number of recursive calls.
"""

def calculate_big_o(recursive_time_complexity, iterative_time_complexity, recursive_calls):
    if recursive_calls == 0:
        return iterative_time_complexity
    return f"O({recursive_calls} * {iterative_time_complexity})" if recursive_time_complexity == "1" else f"O({recursive_time_complexity} + {recursive_calls} * {iterative_time_complexity})"