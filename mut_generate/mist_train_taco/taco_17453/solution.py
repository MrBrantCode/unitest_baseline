"""
QUESTION:
Tim likes Math. He likes it so much that he always brings his tablets with him and reads math e-books everywhere, even during parties.

Tim found an interesting exercise in one of the e-books he is reading. But you want him to join the party, so you decide to answer the question for him.

The problem is: Given D and P, how many ordered pairs of integers are there whose absolute difference is D and whose product is P? In other words, how many pairs of integers (A,B) are there such that:

|A−B|=D
A×B=P

SAMPLE INPUT
3
1 2
0 4
-1 1

SAMPLE OUTPUT
4
2
0
"""

from math import sqrt

def count_ordered_pairs(D, P):
    def factors(n):
        return [(i, n // i) for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
    
    if P == 0:
        return 4 if D == 0 else 0
    
    pairs = factors(P)
    count = 0
    
    for i, j in pairs:
        if abs(i - j) == D:
            count += 1
    
    return count * 2 if count > 0 else 0