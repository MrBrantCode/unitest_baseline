"""
QUESTION:
Create a function `cube_numbers` that takes a list of inputs, cubes each number, stores the results in a list, and returns the sorted list. The function should handle non-numeric inputs by ignoring them and printing an error message. Additionally, provide a function `binary_search` to search for a target value in the sorted list. The functions should have a time complexity of O(n log n) and space complexity of O(n), where n is the number of inputs.
"""

def cube_numbers(inputs):
    """
    Cubes each number in the input list, stores the results in a list, 
    and returns the sorted list. Non-numeric inputs are ignored and an 
    error message is printed.

    Args:
        inputs (list): A list of inputs

    Returns:
        list: A sorted list of cubed numbers
    """
    results = []
    for num in inputs:
        try:
            # Cube the number and append to the results
            result = int(num) ** 3
            results.append(result)
        except ValueError:
            print(f"Ignoring {num}, it's not a valid integer")
    results.sort()
    return results

def binary_search(array, target):
    """
    Searches for a target value in a sorted list using binary search.

    Args:
        array (list): A sorted list of numbers
        target (int): The target value to search for

    Returns:
        int: The index of the target value if found, otherwise None
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = array[mid]
        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            return mid
    return None