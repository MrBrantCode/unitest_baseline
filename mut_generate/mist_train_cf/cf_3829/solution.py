"""
QUESTION:
Given an array of integers, write a function `count_even_before_odd(arr)` to find the number of consecutive even elements that appear before any odd elements. The array can contain both positive and negative integers and can have a length of up to 10^6 with elements ranging from -10^9 to 10^9.
"""

def count_even_before_odd(arr):
    count_even = 0
    for num in arr:
        if num % 2 == 0:
            count_even += 1
        else:
            break
    return count_even