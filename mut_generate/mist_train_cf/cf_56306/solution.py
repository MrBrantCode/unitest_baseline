"""
QUESTION:
Write a function named `count_nums` that takes an array of integers as input and returns the count of elements where the sum of their signed digits (making the first digit negative if the number is negative) is greater than zero and a multiple of 4.
"""

def count_nums(arr):
    def sum_digits(n):
        return sum(int(d) * (-1 if i == 0 and n < 0 else 1) for i, d in enumerate(str(abs(n))))
    
    return sum(1 for n in arr if sum_digits(n) > 0 and sum_digits(n) % 4 == 0)