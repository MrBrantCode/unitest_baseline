"""
QUESTION:
Write a function `count_even_before_odd` that takes an array of integers as input and returns the number of even elements that appear before the first odd element in the array. The array can contain both positive and negative integers, have a length of up to 10^6, and the elements can range from -10^9 to 10^9.
"""

def count_even_before_odd(arr):
    count_even = 0
    found_odd = False

    for num in arr:
        if num % 2 == 0:
            if not found_odd:
                count_even += 1
        else:
            found_odd = True

    return count_even