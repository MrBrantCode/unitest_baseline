"""
QUESTION:
Create a function my_func that takes a list of integers as input and returns the maximum value using recursion and binary search. The length of the list should be between 1 and 10^6, and the integers can range from -10^9 to 10^9. The function should not use built-in functions or libraries to find the maximum value, and the time complexity should be O(n), where n is the length of the list.
"""

def entrance(lst):
    # Base case: if the list contains only one element, return it as the maximum value
    if len(lst) == 1:
        return lst[0]
    
    # Find the midpoint of the list
    mid = len(lst) // 2
    
    # Recursively search for the maximum value in the first half of the list
    max1 = entrance(lst[:mid])
    
    # Recursively search for the maximum value in the second half of the list
    max2 = entrance(lst[mid:])
    
    # Compare the maximum values found in each half and return the larger one
    return max1 if max1 > max2 else max2