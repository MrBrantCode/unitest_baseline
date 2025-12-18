"""
QUESTION:
Refine the function 'count_nums' that takes a list of integers as input and returns a count of elements where the sum of their digits (considering the negative sign as a negative initial digit) is greater than zero and divisible by 4.
"""

def count_nums(arr):
    return sum(1 for num in arr if sum(int(d) for d in str(abs(num))) > 0 and sum(int(d) for d in str(abs(num))) % 4 == 0)