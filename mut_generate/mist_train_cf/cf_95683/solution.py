"""
QUESTION:
Write a function `count_digit` that takes three parameters: `start_num`, `end_num`, and `digit`. The function should return the number of times `digit` appears in numbers within the range from `start_num` to `end_num` (inclusive) that are divisible by 7.
"""

def count_digit(start_num, end_num, digit):
    count = 0
    for num in range(start_num, end_num + 1):
        if num % 7 == 0 and str(digit) in str(num):
            count += 1
    return count