"""
QUESTION:
Write a function `remove_and_calculate_sum` that takes an array of integers as input, removes the element at index 4, and calculates the sum of the remaining elements. The function should apply the following rules before returning the sum:

- If the removed element is greater than 100, multiply the sum of the remaining elements by 3.
- If the removed element is between 50 and 100 (inclusive), subtract 2 from each element in the array before calculating the sum.
- If the removed element is less than 50, add the square of each element in the array to the sum.
"""

def remove_and_calculate_sum(arr):
    removed_element = arr.pop(4)
    total_sum = 0

    if removed_element > 100:
        total_sum = sum(arr) * 3
    elif 50 <= removed_element <= 100:
        total_sum = sum(num - 2 for num in arr)
    else:
        total_sum = sum(num ** 2 for num in arr)

    return total_sum