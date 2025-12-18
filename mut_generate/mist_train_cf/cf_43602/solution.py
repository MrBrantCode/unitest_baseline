"""
QUESTION:
Implement a function `apply_fibonacci_recursively` that takes a nested numeric list as input and returns a new list where each element is the Fibonacci sequence of the corresponding element in the input list. The function should handle nested lists of arbitrary depth and raise an error if the input is not a list or contains non-numeric values.
"""

def apply_fibonacci_recursively(nested_list):
    def fibonacci(n):  
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    def process_list(current_list):
        try:
            return [process_list(i) if isinstance(i, list) else fibonacci(i) for i in current_list]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    
    return process_list(nested_list)