"""
QUESTION:
Find all possible Pythagorean triplets (a, b, c) where a, b, and c are positive integers, 0 < a < b < c, and c < 1,000,000. Write a function num_pythagorean_triplets(limit) that returns the number of such triplets.
"""

import math

def num_pythagorean_triplets(limit):
    count = 0
    m = 2
    while(m * m < limit):
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if(c > limit):
                break
            if(a>0 and b>0 and c>0 and a < b and b<c):
                count += 1
        m += 1
    return count