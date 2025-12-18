"""
QUESTION:
Create a function `calc_fibonacci_number(index)` that calculates the Fibonacci sequence number at a given index. The function should return the Fibonacci number at the specified index, where the Fibonacci sequence is defined as a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def calc_fibonacci_number(index):
    if index == 0 or index == 1:
        return index
    first_num = 0
    second_num = 1
    for i in range(2, index+1):
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num
    return second_num