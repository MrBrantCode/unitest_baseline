"""
QUESTION:
Create a function `advanced_sort(arr)` that takes an array of non-negative integers as input. The function should sort the array in the following manner: 

- First, sort the integers based on the length of their binary equivalents in non-descending order. 
- For integers with the same binary length, sort them based on their numerical values.
- Within each group of integers with the same binary length, sort them based on the cumulative sum of their individual decimal digits.
"""

def advanced_sort(arr):
    return sorted(arr, key=lambda x: (len(bin(x)) - 2, x, sum(int(digit) for digit in str(x))))