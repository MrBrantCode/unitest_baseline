"""
QUESTION:
Write a function `count_digit(start_num, end_num, digit)` that calculates the number of times a specific digit appears in numbers within the range of `start_num` to `end_num` (inclusive) that are divisible by 7. The function should take three parameters: the start of the range, the end of the range, and the digit to be counted.
"""

def count_digit(start_num, end_num, digit):
    count = 0
    for num in range(start_num, end_num + 1):
        if num % 7 == 0 and str(digit) in str(num):
            count += 1
    return count