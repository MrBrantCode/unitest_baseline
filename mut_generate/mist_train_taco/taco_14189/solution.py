"""
QUESTION:
Given an Integer N, write a program to reverse it.

-----Input-----

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N. 

-----Output-----
For each test case, display the reverse of the given number N, in a new line.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000

-----Example-----
Input
4
12345
31203
2123
2300
Output
54321
30213
3212
32
"""

def reverse_integer(N: int) -> int:
    # Remove trailing zeros
    while N % 10 == 0 and N != 0:
        N //= 10
    
    # Convert to string and reverse
    reversed_str = str(N)[::-1]
    
    # Convert back to integer
    reversed_int = int(reversed_str)
    
    return reversed_int