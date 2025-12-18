"""
QUESTION:
Write a function called `sum_even_numbers` that calculates the sum of all even numbers in a given array of integers. The function should use a single loop and have a time complexity of O(n), where n is the number of elements in the array. The space complexity should be O(1). If the array does not contain any even numbers, the function should return 0.
"""

def sum_even_numbers(arr):
    total = 0

    for num in arr:
        if num % 2 == 0:
            total += num

    return total