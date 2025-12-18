"""
QUESTION:
Create a function called `find_largest_number` that takes a list of numbers (integers and/or floating-point numbers) and returns the largest number in the list. The function should ignore any duplicate numbers, truncate floating-point numbers to integers, and exclude negative numbers. If the list is empty or contains any negative numbers, return an error message stating that the list cannot be empty or that negative numbers are not allowed, respectively.
"""

def find_largest_number(lst):
    if not lst:
        return "Error: List cannot be empty."
    
    lst = [int(num) for num in lst if num >= 0]
    
    if not lst:
        return "Error: Negative numbers are not allowed."
    
    largest_num = max(lst)
    return largest_num