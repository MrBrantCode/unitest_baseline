"""
QUESTION:
Create a function named `check_strictly_ascending_order` that takes a list of numbers as input and returns a boolean value indicating whether the list is in strictly ascending order (i.e., each number is greater than its previous number) and contains at least two elements. The function should also handle exceptions for non-numeric values in the list, empty lists, lists with only one element, and any other unexpected errors.
"""

def check_strictly_ascending_order(lst):
    # Handle instances where the list is empty or has only one element
    if not lst or len(lst) == 1:
        print("List needs at least two elements for comparison.")
        return False

    try:
        # traverse through the given list
        for i in range(len(lst) - 1):
            
            # Check if each item is a number
            if not isinstance(lst[i], (int, float)) or not isinstance(lst[i + 1], (int, float)):
                print("Non-numeric values found in list.")
                return False

            # Check if list is in strictly ascending order
            if lst[i] >= lst[i + 1]:
                return False

        return True

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False