"""
QUESTION:
Create a function called `find_largest_number` that takes in a list of numbers. The function should return the largest number in the list after truncating any floating-point numbers to integers and excluding any duplicate numbers. The function should return an error message if the list contains negative numbers or is empty.
"""

def find_largest_number(lst):
    if not lst:
        return "Error: List cannot be empty."
    
    lst = [int(num) for num in lst if num >= 0]
    
    if not lst:
        return "Error: Negative numbers are not allowed."
    
    return max(set(lst))