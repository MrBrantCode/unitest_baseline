"""
QUESTION:
Determine the function F(N) where F(N) denotes the count of doors that remain open after Peter has executed all feasible actions. The function F(N) should take an integer N as input and return the count of open doors. The input N is in the range of 0 to 10^12.
"""

def count_doors(n):
    i, sqrt_n, count = 2, int(n**0.5), 0
    while i <= sqrt_n:
        count += min(i-1, (n//i)-i//2)+1
        i += 2
    return count