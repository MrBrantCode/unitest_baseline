"""
QUESTION:
Create a function named `find_5th_smallest_element` that takes a list of numbers as input, and returns the 5th smallest integer element as a string. The function should handle lists containing duplicate elements, negative numbers, and floating point numbers. If the list is empty or does not contain at least 5 elements, the function should return an error message.
"""

def find_5th_smallest_element(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return "The list is empty."
    
    # Convert all elements to integers and filter out non-integer values
    lst = [int(x) for x in lst if isinstance(x, (int, float))]
    
    # Sort the list in ascending order
    lst.sort()
    
    # Check if the index is out of range
    if len(lst) < 5:
        return "The list does not contain a 5th smallest element."
    
    # Find the 5th smallest element
    fifth_smallest = lst[4]
    
    return str(fifth_smallest)