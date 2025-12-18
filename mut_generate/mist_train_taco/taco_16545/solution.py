"""
QUESTION:
With the college fest approaching soon, Manasa is following a strict dieting regime . Today, she just cannot resist her temptation for having a pizza. An inner conflict ensues, and she decides that she will have a pizza, only if she comes up with a solution to the problem stated below. Help her get the pizza for herself.

Given a list L of N numbers, where 

L = { a_{1}, a_{2}, a_{3}, a_{4} ....  , a_{N}} 

Find the value of M that is computed as described below.  

Input Format 

The first line contains an integer N i.e. size of the list L. 

The next line contains N space separated integers, each representing an element of the list L.  

Output Format 

Print the value of M _modulo (10^{9} + 7)_. 

Constraints 

1 ≤ N ≤ 5100

0 ≤ a_{i} ≤ 10^{15} , where i ∈ [1 .. N]

Sample Input 00  

3
1 2 3

Sample Output 00  

40392

Explanation

There are 8 subsets of given set,

S = {1,2,3} and L - S  ={0} value of F(6) = 19601
S = {1,2} and L - S  ={3} value of F(0) = 1
S = {1,3} and L - S  ={2} value of F(2) = 17
S = {2,3} and L - S  ={1} value of F(4) = 577
S = {1} and L - S  ={2,3} value of F(4) = 577
S = {2} and L - S  ={1,3} value of F(2) = 17
S = {3} and L - S  ={1,2} value of F(0) = 1
S = {} and L - S  ={1,2,3} value of F(6) = 19601

Adding all these values, we get M = 40392.
"""

def calculate_fest_value(numbers):
    """
    Calculate the value M modulo (10^9 + 7) for a given list of numbers.

    Parameters:
    numbers (list of int): A list of integers representing the elements of the list L.

    Returns:
    int: The computed value M modulo (10^9 + 7).
    """
    from collections import Counter
    from functools import reduce
    from itertools import accumulate, combinations, takewhile, product

    modo = 10 ** 9 + 7

    class Lucmat:
        def __init__(s, P, Q, Iv, modo):
            (s.matBase, s.modo, s.pows, po, s.Iv) = ([[P, -Q], [1, 0]], modo, {}, 1, Iv)
            s.pows[1] = s.matBase
            s.mbl = 1
            s.modo = modo

        def sqmatmulmod(s, m1, m2):
            mr = list(([0] * 2 for _ in range(2)))
            for l in range(len(m1)):
                for c in range(len(m1)):
                    mr[l][c] = sum((m1[l][ix] * m2[ix][c] for ix in range(len(m1)))) % s.modo
            return mr

        def do(s, po):
            if po < 2:
                return s.Iv[po]
            for bl in range(s.mbl, po.bit_length()):
                s.pows[bl + 1] = s.sqmatmulmod(s.pows[bl], s.pows[bl])
            s.mbl = po.bit_length()
            pc = 1
            while not po & 1:
                (po, pc) = (po >> 1, pc + 1)
            (rm, pc, po) = (s.pows[pc], pc + 1, po >> 1)
            while po:
                if po & 1:
                    rm = s.sqmatmulmod(s.pows[pc], rm)
                (pc, po) = (pc + 1, po >> 1)
            return rm[0][0] * s.Iv[0] + rm[0][1] * s.Iv[1]

    def faire(s):
        Fm = Lucmat(6, 1, (1, 3), modo)
        r = 1
        for v in s:
            r = 2 * r * Fm.do(v) % modo
        return r

    return faire(numbers)