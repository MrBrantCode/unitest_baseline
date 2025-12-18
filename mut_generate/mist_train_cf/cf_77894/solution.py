"""
QUESTION:
Write a Python function called `amalgamate_integers` that takes a list of integers, reverses their order, converts them to strings, and concatenates them into a single string without any separators.
"""

def amalgamate_integers(lst):
    """Takes a list of integers, reverses their order, converts them to strings, 
    and concatenates them into a single string without any separators."""
    
    # Reverse the list using slicing
    lst = lst[::-1]
    
    # Convert the integers in the list to strings for concatenation
    lst = [str(i) for i in lst]
    
    # Join the strings in the list together with no spaces in between
    result = ''.join(lst)
    
    return result