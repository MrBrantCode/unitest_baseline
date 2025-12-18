"""
QUESTION:
You are given a string, $\mbox{S}$, consisting of lowercase English letters.

A string is beautiful with respect to $\mbox{S}$ if it can be derived from $\mbox{S}$ by removing exactly $2$ characters.

Find and print the number of different strings that are beautiful with respect to $\mbox{S}$.

Input Format

A single string of lowercase English letters denoting $\mbox{S}$.

Constraints

$3\leq|S|\leq10^6$
$3\leq|S|\leq20$ holds for test cases worth at least $15\%$ of the problem's score.
$3\leq|S|\leq2000$ holds for test cases worth at least $30\%$ of the problem's score.

Output Format

Print the number of different strings that are beautiful with respect to $\mbox{S}$.

Sample Input
abba

Sample Output
4

Explanation

$S=\{abba\}$ 

The following strings can be derived by removing $2$ characters from $\mbox{S}$: $ab,bb,ba,ab,ba,aa,\text{and}bb$.

This gives us our set of unique beautiful strings, $B=\{ab,ba,aa,bb\}$. As $|B|=4$, we print $4$.
"""

import operator as op
import functools

def ncr(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = functools.reduce(op.mul, range(n, n - r, -1))
    denom = functools.reduce(op.mul, range(1, r + 1))
    return numer // denom

def count_beautiful_strings(s):
    s += ' '
    n_blocks = 0
    block_size = 0
    count = 0
    prev = None
    prev2 = None
    
    for c in s:
        if prev and c != prev:
            if block_size > 1:
                count += 1
            n_blocks += 1
            block_size = 1
            if c == prev2:
                count -= 1
        else:
            block_size += 1
        prev2 = prev
        prev = c
    
    return ncr(n_blocks, 2) + count