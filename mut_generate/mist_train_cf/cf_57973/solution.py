"""
QUESTION:
Write a function `find_even_before_odd(arr, start_index, end_index)` that takes an array of integers `arr` and a range defined by `start_index` and `end_index` as input. The function should return a tuple containing the count of even numbers, their sum, and their average that appear before the first occurrence of an odd number within the given range. If no even numbers are found before an odd number, the average should be 0. Ensure the function handles invalid input arrays and ranges.
"""

def find_even_before_odd(arr, start_index, end_index):
    # Check validity of the array and indices
    if not arr or start_index < 0 or end_index >= len(arr) or start_index > end_index:
        return 'Invalid input'

    count_even = 0
    sum_even = 0

    for i in range(start_index, end_index + 1):
        if arr[i] % 2 == 0:
            count_even += 1
            sum_even += arr[i]
        else:
            break
    
    average_even = sum_even / count_even if count_even != 0 else 0

    return count_even, sum_even, average_even