"""
QUESTION:
Chef has recently learned about number bases and is becoming fascinated.
Chef learned that for bases greater than ten, new digit symbols need to be introduced, and that the convention is to use the first few letters of the English alphabet. For example, in base 16, the digits are 0123456789ABCDEF. Chef thought that this is unsustainable; the English alphabet only has 26 letters, so this scheme can only work up to base 36. But this is no problem for Chef, because Chef is very creative and can just invent new digit symbols when she needs them. (Chef is very creative.)
Chef also noticed that in base two, all positive integers start with the digit 1! However, this is the only base where this is true. So naturally, Chef wonders: Given some integer N, how many bases b are there such that the base-b representation of N starts with a 1?

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
Each test case consists of one line containing a single integer N (in base ten).

-----Output-----
For each test case, output a single line containing the number of bases b, or INFINITY if there are an infinite number of them.

-----Constraints-----

-----Subtasks-----Subtask #1 (16 points):
- 1 ≤ T ≤ 103
- 0 ≤ N < 103
Subtask #2 (24 points):
- 1 ≤ T ≤ 103
- 0 ≤ N < 106
Subtask #3 (28 points):
- 1 ≤ T ≤ 103
- 0 ≤ N < 1012
Subtask #4 (32 points):
- 1 ≤ T ≤ 105
- 0 ≤ N < 1012

-----Example-----
Input:4
6
9
11
24

Output:4
7
8
14

-----Explanation-----
In the first test case, 6 has a leading digit 1 in bases 2, 4, 5 and 6: 610 = 1102 = 124 = 115 = 106.
"""

import math

def count_bases_starting_with_one(n):
    if n == 1:
        return 'INFINITY'
    
    ans = 0
    x = len(bin(n)) - 2
    
    for j in range(1, x):
        a = math.floor(pow(n / 2, 1 / j))
        b = math.floor(pow(n, 1 / j))
        
        while 2 * a ** j <= n:
            a += 1
        while 2 * (a - 1) ** j > n:
            a -= 1
        while b ** j > n:
            b -= 1
        while (b + 1) ** j <= n:
            b += 1
        
        if b - a + 1 > 0:
            ans += b - a + 1
    
    return ans