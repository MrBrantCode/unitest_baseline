"""
QUESTION:
Implement a function `filter_and_rearrange` that takes in an array of integers `arr` and an integer `n`, and returns a tuple containing the array with all even numbers removed from the first `n` elements, the remaining odd numbers sorted in descending order, and the sum of these odd numbers. If the array is empty or all numbers in the first `n` numbers are even, return an empty array and zero, respectively.
"""

def filter_and_rearrange(arr, n):
    odd_numbers = [num for num in arr[:n] if num % 2 != 0]
    if len(odd_numbers) == 0:
        return [], 0
    else:
        odd_numbers.sort(reverse=True)
        return odd_numbers, sum(odd_numbers)