"""
QUESTION:
A non-decreasing sequence is a called a Fox sequence, iff the most frequent element in the sequence is unique. 

e.g. The sequence 1, 1, 2, 3, 4  is a Fox sequence, because it follows the above definition. The most frequent element is 1. It occurs twice in the series, and is unique.

But the sequence 1, 1, 2, 2 is not a Fox sequence, because there are two most frequent elements - 1 and 2. It violates the uniqueness property.

Note: Sequence 2, 1, 1 is not a Fox sequence, because it is not a non-decreasing sequence.

You need to find the number of all possible Fox sequences of length n with elements having value between lo and hi inclusive.  

As the number can grow very large, return the number modulo (10^{9} + 7).

Input Format 

The first line will contain T, i.e., the number of test cases. 

For each test case, there will be a single line containing three space separated integers n, lo, hi.

Output Format 

For each test case, display a single value corresponding to the number of all possible Fox sequences.

Constraints  

1  ≤ T ≤ 5 

1  ≤ lo, hi ≤ 10^{9} 

lo ≤ hi 

0  ≤ \|hi - lo\| < 10^{5} 

1  ≤ n ≤ 10^{5}  

Sample Input

5
2 1 1
2 1 3
3 1 2
4 4 5
10 2 4

Sample Output

1
3
4
4
60

Explanation 

For the first test case, 1 1 is the only possible Fox sequence. 

For the second test case, 1 1, 2 2, and 3 3 are three possible Fox sequences. 

For the third test case, 1 1 1, 2 2 2, 1 1 2, and 1 2 2 are four possible Fox 

sequences. 

Rest of the test cases are up to you to figure out.
"""

def count_fox_sequences(n: int, lo: int, hi: int) -> int:
    P = 10 ** 9 + 7
    
    # Precompute factorials and their modular inverses
    fact = [1]
    for i in range(1, 200001):
        fact.append(fact[-1] * i % P)
    
    inv = [0, 1]
    for i in range(2, 200001):
        inv.append(P - P // i * inv[P % i] % P)
    
    inv_fact = [1]
    for i in range(1, 100001):
        inv_fact.append(inv_fact[-1] * inv[i] % P)
    
    def ceil_div(a, b):
        return -(-a // b)
    
    def part(n, k):
        if k == 0:
            return 1 if n == 0 else 0
        return C(n + k - 1, n)
    
    def C(n, k):
        return fact[n] * inv_fact[k] % P * inv_fact[n - k] % P if n >= 0 and k >= 0 and (k <= n) else 0
    
    def g(sum, n, b):
        ret = 0
        for i in range(sum // b + 1):
            sign = 1 if i & 1 == 0 else -1
            ret += sign * part(sum - i * b, n) * C(n, i) % P
            ret %= P
        return ret
    
    def f(n, k):
        ret = 0
        for max in range(ceil_div(n + k - 1, k), n + 1):
            ret += g(n - max, k - 1, max)
            ret %= P
        return ret * k % P
    
    # Calculate the number of Fox sequences
    return f(n, hi - lo + 1)