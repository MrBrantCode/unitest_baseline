"""
QUESTION:
Mr. Santa asks all the great programmers of the world to solve a trivial problem. He gives them an integer m and asks for the number of positive integers n, such that the factorial of n ends with exactly m zeroes. Are you among those great programmers who can solve this problem?


-----Input-----

The only line of input contains an integer m (1 ≤ m ≤ 100 000) — the required number of trailing zeroes in factorial.


-----Output-----

First print k — the number of values of n such that the factorial of n ends with m zeroes. Then print these k integers in increasing order.


-----Examples-----
Input
1

Output
5
5 6 7 8 9 
Input
5

Output
0


-----Note-----

The factorial of n is equal to the product of all integers from 1 to n inclusive, that is n! = 1·2·3·...·n.

In the first sample, 5! = 120, 6! = 720, 7! = 5040, 8! = 40320 and 9! = 362880.
"""

import itertools
import bisect

def find_factorials_with_trailing_zeroes(m):
    # Initialize the degrees array
    degs = [0 for i in range(5 * m + 6)]
    deg = 5
    
    # Calculate the number of trailing zeroes for each factorial
    while deg < 5 * m + 1:
        for i in range(deg, 5 * m + 6, deg):
            degs[i] += 1
        deg *= 5
    
    # Calculate the prefix sum of the degrees
    prefix = list(itertools.accumulate(degs))
    
    # Find the first index where the prefix sum is at least m
    i = bisect.bisect_left(prefix, m)
    
    # Collect all n values where the factorial ends with exactly m zeroes
    ans = []
    for j in range(i, min(i + 5, 5 * m + 6)):
        if prefix[j] == m:
            ans.append(j)
    
    # Return the number of such n values and the list of n values
    return len(ans), ans