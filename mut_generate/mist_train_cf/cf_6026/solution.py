"""
QUESTION:
Create a function `my_func` that takes a list of integers and returns the maximum value in the list. Implement the function using recursion and a binary search approach. The function should have a time complexity of O(n) and must not use any built-in functions or libraries to find the maximum value. The list can contain between 1 and 10^6 integers, ranging from -10^9 to 10^9.
"""

def my_func(lst):
    # Base case: if the list contains only one element, return it as the maximum value
    if len(lst) == 1:
        return lst[0]
    
    # Find the midpoint of the list
    mid = len(lst) // 2
    
    # Recursively search for the maximum value in the first half of the list
    max1 = my_func(lst[:mid])
    
    # Recursively search for the maximum value in the second half of the list
    max2 = my_func(lst[mid:])
    
    # Compare the maximum values found in each half and return the larger one
    return max1 if max1 > max2 else max2