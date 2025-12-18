"""
QUESTION:
Find the Nth term of the Mysterious series.
N    Nth term
1    5
2    10
3    26
4    50
5    122
.
.
.
10    842
Example 1:
Input: N = 1
Output: 5 
Explanation: First term of the series is 5.
Example 2:
Input: N = 2
Output: 10
Explanation: Second term of the series is 10. 
Your Task:  
You dont need to read input or print anything. Complete the function nthMysterious() which takes N as input parameter and returns the Nth term of the Mysterious series.
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)
Constraints:
1<= N <=10^{3}
"""

import math

def is_prime(n):
    if n == 0 or n == 1:
        return False
    lim = int(math.sqrt(n)) + 1
    for i in range(2, lim):
        if n % i == 0:
            return False
    return True

def nth_mysterious_term(N):
    res = []
    c = 0
    for i in range(2, int(100000.0) + 1):
        if is_prime(i):
            res.append(i * i + 1)
            c += 1
        if c == N:
            return res[N - 1]