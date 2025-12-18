"""
QUESTION:
Construct a function `seven_mult_seq(m, min_num, max_num)` to calculate the frequency of the digit 7 within ascending sequences of numbers less than `m` and divisible by either 5 or 11, where the sequence starts at `min_num` and ends at `max_num`. The function should return the total count of the digit 7 in all such sequences. The parameters should satisfy the condition that `min_num` is less than or equal to `max_num` and both are positive integers.
"""

def seven_mult_seq(m: int, min_num: int, max_num: int) -> int:
    num = min_num
    count = 0
    while num <= max_num and num < m:
        if num % 5 == 0 or num % 11 == 0:
            count += str(num).count('7')
        num += 1
    return count