"""
QUESTION:
Write a function `count_even_before_odd(arr)` that takes an array of integers as input and returns the number of consecutive even elements that appear before the first odd element. The array can contain both positive and negative integers and can have a length of up to 10^6 with elements ranging from -10^9 to 10^9.
"""

def count_even_before_odd(arr):
    count_even = 0
    for num in arr:
        if num % 2 == 0:
            count_even += 1
        else:
            break
    return count_even