"""
QUESTION:
Write a function named `get_sums` that takes an integer `max_num` as input and returns two values: the sum of all even numbers and the sum of all odd numbers between 0 and `max_num` (exclusive). The function should return the sum of even numbers first, followed by the sum of odd numbers.
"""

def get_sums(max_num):
    total_even = 0
    total_odd = 0
    for i in range(max_num):
        if i % 2 == 0:
            total_even += i
        else:
            total_odd += i
    return total_even, total_odd