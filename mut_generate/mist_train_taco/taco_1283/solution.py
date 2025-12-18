"""
QUESTION:
Nagase is a top student in high school. One day, she's analyzing some properties of special sets of positive integers.

She thinks that a set S = \\{a_{1}, a_{2}, ..., a_{N}\\} of distinct positive integers is called special if for all 1 \leq i \leq N, the gcd (greatest common divisor) of a_{i} and the sum of the remaining elements of S is not 1.

Nagase wants to find a special set of size N. However, this task is too easy, so she decided to ramp up the difficulty. Nagase challenges you to find a special set of size N such that the gcd of all elements are 1 and the elements of the set does not exceed 30000.

Constraints

* 3 \leq N \leq 20000

Input

Input is given from Standard Input in the following format:


N


Output

Output N space-separated integers, denoting the elements of the set S. S must satisfy the following conditions :

* The elements must be distinct positive integers not exceeding 30000.
* The gcd of all elements of S is 1, i.e. there does not exist an integer d > 1 that divides all elements of S.
* S is a special set.



If there are multiple solutions, you may output any of them. The elements of S may be printed in any order. It is guaranteed that at least one solution exist under the given contraints.

Examples

Input

3


Output

2 5 63


Input

4


Output

2 5 20 63
"""

def find_special_set(N):
    M = 30001
    if N == 3:
        return [2, 5, 63]
    
    L = [3, 9]
    N -= 2
    
    if N % 2 == 1:
        L.append(6)
        N -= 1
    
    if N != 0:
        for i in range(2, M, 2):
            if i % 6 == 0:
                continue
            L.append(i)
            N -= 1
            if N == 0:
                break
        
        if N % 2 == 1:
            N += 1
            L.pop()
    
    if N != 0:
        for i in range(15, M, 6):
            L.append(i)
            N -= 1
            if N == 0:
                break
    
    if N % 2 == 1:
        N += 1
        L.pop()
    
    if N != 0:
        for i in range(12, M, 6):
            N -= 1
            L.append(i)
            if N == 0:
                break
    
    if N == 1:
        L.append(6)
    
    return L