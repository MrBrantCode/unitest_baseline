"""
QUESTION:
Write a function `advanced_sort` that sorts a list of positive integers. The function should sort the list in ascending order based on the following criteria:

1. The length of the binary representation of each integer.
2. In cases where two or more integers have the same binary length, sort them based on their decimal values.
3. Further group the integers with similar binary lengths and sort each group based on the sum of the digits in their decimal representation.

The input list only contains non-negative integers, but may include zero.
"""

def advanced_sort(arr):
    def sum_digits(n):
        return sum(int(d) for d in str(n))

    return sorted(sorted(sorted(arr), key=sum_digits), key=lambda n: len(bin(n))-2)