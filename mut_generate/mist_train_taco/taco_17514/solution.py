"""
QUESTION:
Given an integer N,Find  how many strings of length N are possible, consisting only of characters { 'A','B' and 'C' }  with each character {'A','B' and 'C'} occurs at least once.  

Input:
First line of each test case contains number of test cases T. Each test case contains a single integer N.  

Output:
For each test case print the expected output. Output may be too large so print it modulo 10^9+7.

Constraints:
1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^9

SAMPLE INPUT
3
2
3
4

SAMPLE OUTPUT
0
6
36
"""

def count_valid_strings(N: int, mod: int = 1000000007) -> int:
    if N < 3:
        return 0
    return (3 * (pow(3, N-1, mod) - pow(2, N, mod) + 1)) % mod