"""
QUESTION:
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?
Example 1:
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""

def count_consecutive_sum_ways(N: int) -> int:
    res = 1
    while N % 2 == 0:
        N //= 2
    idx = 3
    while idx * idx <= N:
        count = 0
        while N % idx == 0:
            N //= idx
            count += 1
        res *= count + 1
        idx += 2
    return res if N == 1 else res * 2