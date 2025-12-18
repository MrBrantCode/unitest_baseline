"""
QUESTION:
Implement a function `pairExists` that takes in four parameters: an integer `n`, an integer `s`, an integer `d`, and an array `pairs` of size `n`, where each element is an array of two integers. The function should return "YES" if there exists a pair in `pairs` such that the sum of the two integers is greater than `s` and the absolute difference between the two integers is greater than `d`; otherwise, it should return "NO". The function must satisfy the constraints: 1 <= n <= 10^5, 1 <= s <= 10^9, 0 <= d <= 10^9, and -10^9 <= a, b <= 10^9, where `a` and `b` are the integers in each pair.
"""

def pairExists(n, s, d, pairs):
    for pair in pairs:
        if pair[0] + pair[1] > s and abs(pair[0] - pair[1]) > d:
            return "YES"
    return "NO"