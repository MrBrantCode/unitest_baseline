"""
QUESTION:
DJ Boy is a new generation child he has never seen numeric keypad of mobile. So one day when Prem showed him his mobile, DJ boy started laughing on him. Prem being smart gave him a problem to solve with some condition. Your task is to help DJ boy to solve this problem:

Given a number N, DJ boy has to tell how many numbers of length N are possible.

Conditions:

1)He can only press digit that are adjacent i.e. to the left, right, up or bottom to current digit.

2)He may press the same key again i.e. numbers like 000 & 080 are possible for length 3.

3)He cannot press * and # keys.

Constraints:

1 ≤ t ≤ 100

0 ≤ N ≤ 10000

MOD: 10^9 + 9

Input:

First line contains T,the number of test cases.
Next t lines contain a number N.

Output:

Print the required number modulo MOD.

SAMPLE INPUT
2
1
2

SAMPLE OUTPUT
10
36
"""

def count_possible_numbers(N: int) -> int:
    maxn = 10000
    mod = 10**9 + 9
    
    # Initialize the dynamic programming table
    d = [[0] * (maxn + 1) for _ in range(10)]
    
    # Base case: for length 1, there is exactly one number for each digit
    for i in range(10):
        d[i][1] = 1
    
    # Fill the dynamic programming table
    for z in range(2, maxn + 1):
        d[0][z] = (d[0][z-1] + d[8][z-1]) % mod
        d[1][z] = (d[1][z-1] + d[2][z-1] + d[4][z-1]) % mod
        d[2][z] = (d[2][z-1] + d[1][z-1] + d[5][z-1] + d[3][z-1]) % mod
        d[3][z] = (d[3][z-1] + d[2][z-1] + d[6][z-1]) % mod
        d[4][z] = (d[4][z-1] + d[1][z-1] + d[5][z-1] + d[7][z-1]) % mod
        d[5][z] = (d[5][z-1] + d[2][z-1] + d[4][z-1] + d[6][z-1] + d[8][z-1]) % mod
        d[6][z] = (d[6][z-1] + d[3][z-1] + d[5][z-1] + d[9][z-1]) % mod
        d[7][z] = (d[7][z-1] + d[4][z-1] + d[8][z-1]) % mod
        d[8][z] = (d[8][z-1] + d[5][z-1] + d[7][z-1] + d[9][z-1] + d[0][z-1]) % mod
        d[9][z] = (d[9][z-1] + d[6][z-1] + d[8][z-1]) % mod
    
    # Calculate the result for length N
    result = sum(d[i][N] for i in range(10)) % mod
    return result