"""
QUESTION:
Write a function named `process_list` that takes a list of numbers as input, makes all elements positive, removes duplicates, and sorts the list in descending order. The function should handle empty input and non-numeric elements by printing an error message and returning without modifying the original list.
"""

def process_list(lst):
    # Check for empty input
    if not lst:
        print("Empty input!")
        return
    
    # Check for non-numeric elements
    try:
        lst = [float(x) for x in lst]
    except ValueError:
        print("Non-numeric elements found!")
        return
    
    # Make all elements positive
    lst = [abs(x) for x in lst]
    
    # Remove duplicates
    lst = list(set(lst))
    
    # Sort in descending order
    lst.sort(reverse=True)
    
    return lst