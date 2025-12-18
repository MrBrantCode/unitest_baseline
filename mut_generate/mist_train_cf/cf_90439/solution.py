"""
QUESTION:
Implement a function called `remove_and_calculate_sum` that takes an array of integers as input, removes the element at index 4, calculates the sum of the remaining elements, and applies the following conditions: 

- If the removed element is greater than 100, multiply the sum by 3.
- If the removed element is between 50 and 100 (inclusive), subtract 2 from each element before calculating the sum.
- If the removed element is less than 50, add the square of each element to the sum.

The function should return the final sum after applying the conditions.
"""

def remove_and_calculate_sum(arr):
    """
    Removes the element at index 4 from the given array, calculates the sum of the remaining elements,
    and applies conditions based on the removed element.

    If the removed element is greater than 100, multiplies the sum by 3.
    If the removed element is between 50 and 100 (inclusive), subtracts 2 from each element before calculating the sum.
    If the removed element is less than 50, adds the square of each element to the sum.

    Args:
        arr (list): The input array of integers.

    Returns:
        int: The final sum after applying the conditions.
    """

    removed_element = arr.pop(4)
    sum_of_elements = 0

    if removed_element > 100:
        sum_of_elements = sum(arr) * 3
    elif 50 <= removed_element <= 100:
        sum_of_elements = sum(num - 2 for num in arr)
    else:
        sum_of_elements = sum(num ** 2 for num in arr)

    return sum_of_elements