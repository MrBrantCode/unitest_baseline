"""
QUESTION:
Problem description.
Winston and Royce love sharing memes with each other. They express the amount of seconds they laughed ar a meme as the number of ‘XD’ subsequences in their messages. Being optimization freaks, they wanted to find the string with minimum possible length and having exactly the given number of ‘XD’ subsequences.

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases.
- Next T lines contains a single integer N, the no of seconds laughed.

-----Output-----
- 
For each input, print the corresponding string having minimum length. If there are multiple possible answers, print any.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 109
- 1 ≤ Sum of length of output over all testcases ≤ 5*105

-----Example-----
Input:
1
9

Output:
XXXDDD

-----Explanation-----
Some of the possible strings are - XXDDDXD,XXXDDD,XDXXXDD,XDXDXDD etc. Of these, XXXDDD is the smallest.
"""

import math

def generate_min_length_string(n: int) -> str:
    if math.sqrt(n) % 1.0 == 0:
        y = int(math.sqrt(n))
        l = ['X'] * y + ['D'] * y
        return ''.join(l)
    else:
        count = 0
        for x in range(1, int(math.sqrt(n)) + 3):
            if x ** 2 > n:
                break
        x = x - 1
        b = x
        while b * x < n:
            b += 1
        l = ['X'] * b + ['D'] * x
        f = l.index('D')
        l.pop(f)
        l.insert(f - (b * x - n), 'D')
        return ''.join(l)