"""
QUESTION:
Create a function `check_ascending_order(lst)` that checks if a list of numerical values is in ascending order. The function should handle exceptions for inputs that are not numeric and lists that are empty. It should also handle nested lists, where each nested list is also checked for ascending order. The function should return `True` if the list is in ascending order and `False` otherwise.
"""

def check_ascending_order(lst):
    # Check if list is empty
    if not lst:
        return True
        
    # Iterate over list
    for i in range(len(lst)):
        # Check if item in list is numeric
        try:
            if isinstance(lst[i], list):
                # Recursive call for nested list
                if not check_ascending_order(lst[i]):
                    return False
            elif i > 0 and lst[i] < lst[i - 1]:
                return False
        except TypeError:
            print("Error: List contains non-numeric value")
            return False
            
    return True