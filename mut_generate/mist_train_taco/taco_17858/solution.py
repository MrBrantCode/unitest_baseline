"""
QUESTION:
There are N non-negative integers written on a blackboard. The i-th integer is A_i.
Takahashi can perform the following two kinds of operations any number of times in any order:
 - Select one integer written on the board (let this integer be X). Write 2X on the board, without erasing the selected integer.
 - Select two integers, possibly the same, written on the board (let these integers be X and Y). Write X XOR Y (XOR stands for bitwise xor) on the blackboard, without erasing the selected integers.
How many different integers not exceeding X can be written on the blackboard? We will also count the integers that are initially written on the board.
Since the answer can be extremely large, find the count modulo 998244353.

-----Constraints-----
 - 1 \leq N \leq 6
 - 1 \leq X < 2^{4000}
 - 1 \leq A_i < 2^{4000}(1\leq i\leq N)
 - All input values are integers.
 - X and A_i(1\leq i\leq N) are given in binary notation, with the most significant digit in each of them being 1.

-----Input-----
Input is given from Standard Input in the following format:
N X
A_1
:
A_N

-----Output-----
Print the number of different integers not exceeding X that can be written on the blackboard.

-----Sample Input-----
3 111
1111
10111
10010

-----Sample Output-----
4

Initially, 15, 23 and 18 are written on the blackboard. Among the integers not exceeding 7, four integers, 0, 3, 5 and 6, can be written.
For example, 6 can be written as follows:
 - Double 15 to write 30.
 - Take XOR of 30 and 18 to write 12.
 - Double 12 to write 24.
 - Take XOR of 30 and 24 to write 6.
"""

def count_different_integers(N, X, A):
    MOD = 998244353
    
    # Convert binary strings to integers
    X = int(X, 2)
    A = [int(ai, 2) for ai in A]
    
    def gcd(a, b):
        while b:
            if a < b:
                a, b = b, a
                continue
            a ^= b << (a.bit_length() - b.bit_length())
        return a
    
    v = 0
    for ai in A:
        v = gcd(ai, v)
    
    p2 = [1]
    for _ in range(5000):
        p2.append(p2[-1] * 2 % MOD)
    
    dv = v.bit_length()
    dx = X.bit_length()
    
    def dfs(x, y, d):
        if d < dv:
            return int(x >= y)
        else:
            bx = x >> (d - 1) & 1
            by = y >> (d - 1) & 1
            if bx and by:
                return (p2[d - dv] + dfs(x, y, d - 1)) % MOD
            elif not bx and by:
                return dfs(x, y ^ (v << (d - dv)), d - 1)
            elif not by and bx:
                return (p2[d - dv] + dfs(x, y ^ (v << (d - dv)), d - 1)) % MOD
            else:
                return dfs(x, y, d - 1)
    
    return dfs(X, 0, dx)