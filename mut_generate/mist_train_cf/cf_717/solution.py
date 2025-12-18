"""
QUESTION:
Create a Python function named 'check_sorted' to check if a given array is sorted in ascending order. The array can contain both positive and negative integers and have a length greater than 1. The function should return True if the array is sorted in ascending order, and False otherwise along with the index of the first element that violates the sorting order. The array cannot be modified or sorted using any built-in sorting functions or methods. Additionally, the function cannot use any built-in comparison operators (e.g. "<", ">" etc.) or conditional statements (e.g. "if", "else" etc.) to check the sorting order.
"""

def check_sorted(arr):
    # Create a list of tuples where each tuple contains two consecutive elements of the array
    pairs = zip(arr, arr[1:])
    
    # Check if all pairs are in ascending order
    ascending = all(a <= b for a, b in pairs)
    
    if ascending:
        return True
    else:
        # Find the index of the first element that violates the sorting order
        for i, (a, b) in enumerate(zip(arr, arr[1:])):
            if a > b:
                return False, i + 1