"""
QUESTION:
Write a function `five_div_seq(n)` that calculates the occurrence rate of the digit 5 in integers less than `n`, which are divisible by either 9 or 14, have 3 or more digits, and form a descending arithmetic sequence with an even decrement. The function should only consider numbers with a consistent decrement of even value, but does not need to verify if the numbers form a perfect arithmetic sequence.
"""

def five_div_seq(n: int) -> int:
    count = 0
    _, *a, _ = [i for i in range(n, 0, -2) if i % 9 == 0 or i % 14 == 0 and len(str(i)) >= 3]
    for num in a:
        count += str(num).count('5')
    return count