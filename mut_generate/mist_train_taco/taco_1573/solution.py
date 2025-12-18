"""
QUESTION:
Maxim loves to fill in a matrix in a special manner. Here is a pseudocode of filling in a matrix of size (m + 1) × (m + 1):

[Image]

Maxim asks you to count, how many numbers m (1 ≤ m ≤ n) are there, such that the sum of values in the cells in the row number m + 1 of the resulting matrix equals t.

Expression (x xor y) means applying the operation of bitwise excluding "OR" to numbers x and y. The given operation exists in all modern programming languages. For example, in languages C++ and Java it is represented by character "^", in Pascal — by "xor".


-----Input-----

A single line contains two integers n and t (1 ≤ n, t ≤ 10^12, t ≤ n + 1).

Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specifier.


-----Output-----

In a single line print a single integer — the answer to the problem. 


-----Examples-----
Input
1 1

Output
1

Input
3 2

Output
1

Input
3 3

Output
0

Input
1000000000000 1048576

Output
118606527258
"""

def count_special_matrices(n: int, t: int) -> int:
    s = bin(n + 2)[2:]
    l = len(s)
    
    if t & (t - 1):
        return 0
    
    t = t.bit_length()
    f = [[0] * (l + 1) for _ in range(l + 1)]
    
    for i in range(l + 1):
        f[i][0] = f[i][i] = 1
        for j in range(1, i):
            f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
    
    ans = c = 0
    for i in range(l):
        if s[i] == '1':
            if t - c <= l - i - 1:
                ans += f[l - i - 1][t - c]
            c += 1
    
    if t == 1:
        ans -= 1
    
    return ans