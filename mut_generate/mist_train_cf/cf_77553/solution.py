"""
QUESTION:
Given a string `n` representing a positive decimal integer, write a function `min_partitions(n: str)` that returns a tuple containing the minimum number of positive deci-binary numbers (numbers with only digits 0 or 1 and no leading zeros) needed to sum up to `n` and a list of these deci-binary numbers. The function should work under the constraints that `1 <= n.length <= 10^5` and `n` consists of only digits with no leading zeros.
"""

def min_partitions(n: str) -> (int, [int]):
    num = int(max(n))
    arr = [int('1'*len(n))]*num
    return num, arr