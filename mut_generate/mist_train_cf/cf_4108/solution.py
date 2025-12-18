"""
QUESTION:
Create a function called `calculate_cumulative_sum` that takes a list of numbers as input. The function should calculate the cumulative sum of the input list, but only for positive integers greater than 1. The function should return an error message if the list contains any negative numbers, non-integer elements, or zeros. The function should also remove duplicate elements from the input list before performing the calculations and return the cumulative sum in reverse order.
"""

def calculate_cumulative_sum(lst):
    # Check for negative numbers, non-integer elements, or zeros
    if any(num <= 0 or not isinstance(num, int) for num in lst):
        return "Error: Input list should only contain positive integers greater than 1"
    
    # Remove duplicate elements
    unique_lst = list(set(lst))
    
    # Sort the list in descending order
    unique_lst.sort(reverse=True)
    
    # Calculate cumulative sum in reverse order
    cumulative_sum = []
    total = 0
    for num in unique_lst:
        total += num
        cumulative_sum.append(total)
    
    return cumulative_sum