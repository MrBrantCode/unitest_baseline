"""
QUESTION:
Create a Python function named `check_ascending_order` that takes a list of numerical entities as input. The function should return `True` if the list is in ascending order, `False` if it's not, and an error message if the list is empty or contains non-numeric inputs.
"""

def check_ascending_order(lst):
    # Check if list is not empty
    if not lst:
        return "The list is empty"
    else:
        try:
            # Try to convert each element to float
            lst = [float(i) for i in lst]
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    return False
            return True
        except ValueError:
            return "The list contains non-numeric inputs"