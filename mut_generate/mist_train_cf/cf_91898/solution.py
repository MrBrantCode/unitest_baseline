"""
QUESTION:
Write a function named `count_even_before_odd` that takes an array of integers as input. The function should count and return the number of even elements in the array before the first odd element is encountered. The array may contain up to 10^6 elements with values ranging from -10^9 to 10^9.
"""

def count_even_before_odd(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
        else:
            break
    return count