"""
QUESTION:
Create a function named `square_exclude_divisible_by_3` that takes an array of integers as input and returns a new array. For each number in the input array, if the number is divisible by 3, append its square root to the new array; otherwise, append the square of the number.
"""

def square_exclude_divisible_by_3(arr):
    """
    This function takes an array of integers and returns a new array.
    For each number in the input array, if the number is divisible by 3, 
    it appends its square root to the new array; otherwise, it appends the square of the number.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A new list with the transformed numbers.
    """
    new_arr = []
    for num in arr:
        if num % 3 == 0:
            new_arr.append(num ** 0.5)
        else:
            new_arr.append(num ** 2)
    return new_arr