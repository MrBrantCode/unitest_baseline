"""
QUESTION:
Two positive integers a and b have a sum of s and a bitwise XOR of x. How many possible values are there for the ordered pair (a, b)?


-----Input-----

The first line of the input contains two integers s and x (2 ≤ s ≤ 10^12, 0 ≤ x ≤ 10^12), the sum and bitwise xor of the pair of positive integers, respectively.


-----Output-----

Print a single integer, the number of solutions to the given conditions. If no solutions exist, print 0.


-----Examples-----
Input
9 5

Output
4

Input
3 3

Output
2

Input
5 2

Output
0



-----Note-----

In the first sample, we have the following solutions: (2, 7), (3, 6), (6, 3), (7, 2).

In the second sample, the only solutions are (1, 2) and (2, 1).
"""

def count_ordered_pairs(s: int, x: int) -> int:
    if x > s:
        return 0
    
    b = s - x
    if b < 0:
        return 0
    
    a_bin = bin(x)[2:]
    b_bin = bin(b)[2:]
    
    al = len(a_bin)
    bl = len(b_bin)
    
    if bl > al:
        a_bin = '0' * (bl - al) + a_bin
    else:
        b_bin = '0' * (al - bl) + b_bin
    
    for i in range(len(b_bin) - 1):
        if b_bin[i] == '1' and a_bin[i + 1] == '1':
            return 0
    
    if b_bin[-1] == '1':
        return 0
    
    if s == x:
        return 2 ** a_bin.count('1') - 2
    elif x == 0:
        return 1
    else:
        return 2 ** a_bin.count('1')