"""
QUESTION:
Vasya decided to pass a very large integer n to Kate. First, he wrote that number as a string, then he appended to the right integer k — the number of digits in n. 

Magically, all the numbers were shuffled in arbitrary order while this note was passed to Kate. The only thing that Vasya remembers, is a non-empty substring of n (a substring of n is a sequence of consecutive digits of the number n).

Vasya knows that there may be more than one way to restore the number n. Your task is to find the smallest possible initial integer n. Note that decimal representation of number n contained no leading zeroes, except the case the integer n was equal to zero itself (in this case a single digit 0 was used).


-----Input-----

The first line of the input contains the string received by Kate. The number of digits in this string does not exceed 1 000 000.

The second line contains the substring of n which Vasya remembers. This string can contain leading zeroes. 

It is guaranteed that the input data is correct, and the answer always exists.


-----Output-----

Print the smalles integer n which Vasya could pass to Kate.


-----Examples-----
Input
003512
021

Output
30021

Input
199966633300
63

Output
3036366999
"""

import math
from collections import Counter

def find_smallest_integer(received_string, remembered_substring):
    s = list(map(int, received_string))
    t = list(map(int, remembered_substring))
    m = len(s)
    
    # Binary search to find the smallest possible length of n
    (x, y) = (0, m)
    z = (x + y) // 2
    while z != x:
        if z + math.floor(math.log10(z)) + 1 <= m:
            x = z
        else:
            y = z
        z = (x + y) // 2
    m1 = z
    
    k = math.floor(math.log10(m1)) + 1
    D = Counter(s)
    D.subtract(list(map(int, str(m1))))
    D.subtract(t)
    
    try:
        c1 = min((i for i in range(1, 10) if D[i] > 0))
        c2 = t[0]
        D[c1] -= 1
        _prefix = [c1]
        for c in range(c2):
            _prefix += [c] * D[c]
        _suffix = []
        for c in range(c2 + 1, 10):
            _suffix += [c] * D[c]
        num = ''.join([str(c2)] * D[c2])
        prefix = ''.join(map(str, _prefix))
        suffix = ''.join(map(str, _suffix))
        if c2 == 0:
            return min(prefix + remembered_substring + num + suffix, prefix + num + remembered_substring + suffix)
        else:
            D[c1] += 1
            st = []
            for c in range(10):
                st += [c] * D[c]
            return min(prefix + remembered_substring + num + suffix, prefix + num + remembered_substring + suffix, remembered_substring + ''.join(map(str, st)))
    except ValueError:
        return remembered_substring + '0' * D[0]