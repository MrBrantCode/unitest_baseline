"""
QUESTION:
Write a function `five_div_seq(n)` that returns the total count of the digit 5 in integers less than n that are divisible by 9 or 14 and form a decreasing arithmetic progression. The function should only consider integers from n-1 down to 0, and the decreasing arithmetic progression should have a common difference of 1.
"""

def five_div_seq(n: int) -> int:
    total_count = 0

    for i in range(n-1, 0, -1):
        if i % 9 == 0 or i % 14 == 0:
            total_count += str(i).count('5')

    return total_count