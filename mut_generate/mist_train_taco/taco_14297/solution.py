"""
QUESTION:
Given three positive integers N, A and B (A < B < N), find the sum of all positive integers less than N, which are divisible by either A or B.

For example, when N = 20, A = 4 and B = 7, the possible values are 4, 7, 8, 12, 14, and 16. Their sum is 61.
Input Format
The only line of the input file contains three space separated integers N, A and B.

Output Format
Output the required sum.

Constraints
10 ≤ N ≤ 50000
2 ≤ A < B < N

SAMPLE INPUT
20 4 7

SAMPLE OUTPUT
61
"""

def sum_divisible_by_a_or_b(N, A, B):
    total_sum = 0
    for i in range(N):
        if i % A == 0 or i % B == 0:
            total_sum += i
    return total_sum