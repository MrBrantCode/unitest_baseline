"""
QUESTION:
Write a function named `remove_even_duplicates` that takes an array of numbers as input. The function should return a new array containing only the unique odd numbers from the input array, in any order. If the input array is empty or only contains even numbers, the function should return an empty array. The input array can contain both positive and negative numbers and be of any length.
"""

def remove_even_duplicates(arr):
    """
    Returns a new array containing only the unique odd numbers from the input array.
    
    Args:
        arr (list): The input array of numbers.
    
    Returns:
        list: A new array containing unique odd numbers.
    """
    # Check if the array is empty or contains only even numbers
    if not arr or all(num % 2 == 0 for num in arr):
        return []

    # Remove even numbers and duplicates from the array
    result = []
    seen = set()
    for num in arr:
        if num % 2 != 0 and num not in seen:
            result.append(num)
            seen.add(num)

    return result