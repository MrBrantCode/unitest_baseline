"""
QUESTION:
Tim likes Math. He likes it so much that he always brings his tablets with him and reads math e-books everywhere, even during parties.

Tim found an interesting exercise in one of the e-books he is reading. But you want him to join the party, so you decide to answer the question for him.

The problem is: Given ${D}$ and ${P}$, how many ordered pairs of integers are there whose absolute difference is ${D}$ and whose product is ${P}$? In other words, how many pairs of integers $(A,B)$ are there such that:

$|A-B|=D$
$A\times B=P$

Input Format

The first line of input contains ${T}$, the number of test cases. The next ${T}$ lines describe the test cases.

Each test case consists of a single line containing two integers ${D}$ and ${P}$ separated by a single space.

Output Format

For each test case, output a single line containing a single integer which is the answer for that test case.

Constraints  

$1\leq T\leq20000$ 

$|D|\leq10^9$ 

$|P|\leq10^9$  

Sample Input
3
1 2
0 4
-1 1

Sample Output
4
2
0

Explanation

Case 1: There are four pairs of integers with absolute difference ${1}$ and product $2$, namely $(1,2)$, $(2,1)$, $(-1,-2)$, $(-2,-1)$.

Case 2: There are two pairs of integers with absolute difference ${0}$ and product ${4}$, namely $(2,2)$, $(-2,-2)$.

Case 3: There are no pairs of integers with absolute difference $-1$, because the absolute value is never negative.
"""

from math import sqrt

def count_ordered_pairs(d, p):
    if d < 0:
        return 0
    
    ret = set()
    D1 = d * d + 4 * p
    
    if D1 >= 0:
        a = round((d - sqrt(D1)) / 2)
        if a * (d - a) == -p:
            ret.add((a, d - a))
        
        a = round((d + sqrt(D1)) / 2)
        if a * (d - a) == -p:
            ret.add((a, d - a))
        
        a = round((-d - sqrt(D1)) / 2)
        if a * (-d - a) == -p:
            ret.add((a, -d - a))
        
        a = round((-d + sqrt(D1)) / 2)
        if a * (-d - a) == -p:
            ret.add((a, -d - a))
    
    return len(ret)