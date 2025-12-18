"""
QUESTION:
Write a function `square_sum` that takes an integer `num` as input and returns the square of the sum of all unique multiples of 3 or 5 below `num`.
"""

def square_sum(num):
    return sum(set(range(3, num, 3)) | set(range(5, num, 5))) ** 2