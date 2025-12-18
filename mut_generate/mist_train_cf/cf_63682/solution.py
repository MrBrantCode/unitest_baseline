"""
QUESTION:
Create a function named `sort_descend` that takes a list of mixed data types as input. The function should filter out any non-numeric elements from the list, convert numeric strings to floats, and then sort the remaining numbers in descending order. The function should be efficient and able to handle a large amount of data without causing memory errors.
"""

def sort_descend(numeric_list):
    numeric_list = [x if isinstance(x, (int, float)) else float(x) 
                    for x in numeric_list 
                    if (isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.','').isnumeric()))]
                    
    sorted_list = sorted(numeric_list, reverse=True)
    return sorted_list