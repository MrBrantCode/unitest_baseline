"""
QUESTION:
Kate has finally calmed down and decides to forgive Little Deepu, but she won't forgive him just like that. She agrees to forgive him on the grounds that he can solve a mathematical question for her. 
She gives Deepu a large number N and a prime number P and asks him to calculate ((3*N)! / (3!^N) )%P.Your task is to help Little Deepu get back together with Kate.

Input
First line contains number of test cases T.
Next T lines contain two integers N and P, where P is a prime.  

Output
For each test case output the result ( (3*N)! / (3!)^N ) % P.  

Constraints:
1 ≤ T ≤ 10000
1 ≤ N ≤ 333333333
1 ≤ P ≤ 1000000000
1 ≤ abs(3*N-P) ≤ 1000  

SAMPLE INPUT
2
3 11
2 11

SAMPLE OUTPUT
8
9
"""

import math

def calculate_forgiveness_value(N, P):
    # Precompute factorials up to 100 for efficiency
    fa = [1]
    for i in range(1, 100):
        fa.append(i * fa[i-1])
    
    if P == 2:
        num = fa[3 * N]
        den = pow(6, N, P)
        return (num * den) % 2
    else:
        den = pow(6, N, P)
        den = pow(den, P - 2, P)
        num = 0
        if 3 * N < P:
            num = 1
            for i in range(3 * N + 1, P):
                num = (num * i) % P
            num = pow(num, P - 2, P)
        return (num * (P - 1) * den) % P