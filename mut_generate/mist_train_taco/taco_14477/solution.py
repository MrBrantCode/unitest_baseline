"""
QUESTION:
Takahashi has two positive integers A and B.

It is known that A plus B equals N. Find the minimum possible value of "the sum of the digits of A" plus "the sum of the digits of B" (in base 10).

Constraints

* 2 ≤ N ≤ 10^5
* N is an integer.

Input

Input is given from Standard Input in the following format:


N


Output

Print the minimum possible value of "the sum of the digits of A" plus "the sum of the digits of B".

Examples

Input

15


Output

6


Input

100000


Output

10
"""

def min_sum_of_digits(N):
    def sum_of_digits(x):
        return sum(int(digit) for digit in str(x))
    
    min_sum = float('inf')
    
    for A in range(1, N):
        B = N - A
        current_sum = sum_of_digits(A) + sum_of_digits(B)
        if current_sum < min_sum:
            min_sum = current_sum
    
    return min_sum