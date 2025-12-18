"""
QUESTION:
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.


    Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


Credits:Special thanks to @memoryless for adding this problem and creating all test cases.
"""

def count_numbers_with_unique_digits(n: int) -> int:
    if n == 0:
        return 1
    
    ls = [1, 10, 91]
    mul = 9
    for i in range(8):
        mul = 9
        m = 9
        for j in range(i + 2):
            mul *= m
            m -= 1
        ls.append(mul + ls[-1])
    
    if n >= 9:
        return ls[9]
    else:
        return ls[n]