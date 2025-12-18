"""
QUESTION:
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.


Credits:Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""

def calculate_sum_without_plus_minus(a: int, b: int) -> int:
    max_val = 2147483647
    mask = 4294967295
    while b != 0:
        (a, b) = ((a ^ b) & mask, (a & b) << 1 & mask)
    return a if a <= max_val else ~(a ^ mask)