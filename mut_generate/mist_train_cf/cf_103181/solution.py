"""
QUESTION:
Write a function `count_even_before_odd` that takes an array of integers as input and returns the number of even elements that appear before any odd elements. The array can contain both positive and negative integers, with a length of up to 10^6 and element values ranging from -10^9 to 10^9.
"""

def count_even_before_odd(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
        else:
            break
    return count