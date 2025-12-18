"""
QUESTION:
Create a function named `sum_excluding_self` that takes a list of integers as input and returns a new list. Each element in the new list should be the sum of all numbers in the original list, excluding the number at its own index. Implement error handling to check for empty lists and non-integer values, printing an error message in these cases.
"""

def sum_excluding_self(lst):
    if not lst:
        return "Error: List is empty."
    
    for i in lst:
        if not isinstance(i, int):
            return f"Error: List contains non-integer value {i}."
    
    result = []
    total_sum = sum(lst)
    
    for num in lst:
        result.append(total_sum - num)
    
    return result