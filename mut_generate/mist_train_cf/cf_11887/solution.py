"""
QUESTION:
Design a function `arrange_odd_even` that rearranges an array of numbers such that all odd numbers come before even numbers, without using any extra space. The function should have a time complexity of O(n) and maintain the relative order of the numbers within each category.
"""

def arrange_odd_even(arr):
    """
    Rearranges an array of numbers such that all odd numbers come before even numbers.
    
    The function maintains the relative order of the numbers within each category and 
    does not use any extra space. It has a time complexity of O(n).

    Args:
        arr (list): A list of integers.

    Returns:
        list: The rearranged list with odd numbers before even numbers.
    """

    next_even = 0  # index for even numbers
    next_odd = len(arr) - 1  # index for odd numbers

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:  # if current number is even
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]  # swap with last element
            next_odd -= 1
        else:
            next_even += 1
    
    return arr