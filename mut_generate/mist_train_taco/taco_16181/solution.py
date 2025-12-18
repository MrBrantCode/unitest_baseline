"""
QUESTION:
Given K prime numbers and T queries of form Ai, Bi, for each query print the number of integers between Ai and Bi (both inclusive) that are divisible by atleast one of the K given primes.     

Input
First line: K and T. 
Second line: K primes.
Next T lines, each contain Ai, Bi.    

Output
Print T lines, denoting the answer to each of the T queries.

Constraints
1 ≤ K ≤ 10 
1 ≤ T ≤ 100 
1 ≤ A ≤ B ≤ 10^9 
Each prime ≤ 10^7

SAMPLE INPUT
2 1
2 3
1 10

SAMPLE OUTPUT
7

Explanation

2,3,4,6,8,9,10 are the 7 numbers.
"""

from itertools import combinations

def count_divisibles_in_range(k, primes, queries):
    # Generate all combinations of primes
    final = []
    for i in range(1, k + 1):
        arr = combinations(primes, i)
        for item in arr:
            final.append(item)
    
    results = []
    for a, b in queries:
        count = 0
        i = 0
        while i < len(final):
            prod = 1
            for ir in final[i]:
                prod *= ir
            if len(final[i]) % 2 == 1:
                count += (b // prod) - ((a - 1) // prod)
            else:
                count -= (b // prod) - ((a - 1) // prod)
            i += 1
        results.append(count)
    
    return results