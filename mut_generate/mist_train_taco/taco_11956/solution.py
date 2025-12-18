"""
QUESTION:
The Ulam sequence `U` is defined by `u0 = u`, `u1 = v`, with the general term `uN` for `N > 2` given by the least integer expressible uniquely as the sum of two distinct earlier terms. In other words, the next number is always the smallest, unique sum of any two previous terms.

Complete the function that creates an Ulam Sequence starting with the given `u0` and `u1`, and contains `n` terms.

## Example

The first 10 terms of the sequence `U(u0=1, u1=2)` are: 1, 2, 3, 4, 6, 8, 11, 13, 16, 18.

Let's see it in details:
* The first term after the initial 1, 2 is obviously 3, because 1 + 2 = 3
* The next term is 1 + 3 = 4 (we don't have to worry about 4 = 2 + 2 since it is a sum of a *single term* instead of *distinct terms*)
* 5 is not a member of the sequence since it is representable in two ways: 1 + 4 and 2 + 3
* 6 is a memeber, as 2 + 4 = 6
* etc.


Description Reference: http://mathworld.wolfram.com/UlamSequence.html

---

Performance version: https://www.codewars.com/kata/ulam-sequences-performance-edition
"""

from itertools import combinations
from collections import defaultdict

def generate_ulam_sequence(u0, u1, n):
    # Initialize the sequence with the first two terms and their sum
    seq = [u0, u1, u0 + u1]
    
    # Continue generating terms until the sequence has `n` terms
    while len(seq) < n:
        candidates = defaultdict(int)
        
        # Generate all possible sums of two distinct terms in the current sequence
        for (a, b) in combinations(seq, 2):
            candidates[a + b] += 1
        
        # Find the smallest number that can be uniquely represented as a sum of two distinct terms
        for num, pairs in sorted(candidates.items()):
            if num > seq[-1] and pairs == 1:
                seq.append(num)
                break
    
    # Return the first `n` terms of the sequence
    return seq[:n]