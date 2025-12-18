"""
QUESTION:
Mansi is fond of solving mental ability questions. Today while solving some questions she came across a series which she was unable to solve. Help her to find the nth term of the series.
n  nth term
1  3
2  8
3  18
4  32
5  60
.
.
.
10  300
Example 1:
Input: n = 1
Output: 3 
Explanation: The first term of the series is 3.
Example 2:
Input: n = 2
Output: 8
Explanation: The second term of the series is 3. 
Your Task:  
You dont need to read input or print anything. Complete the function nthTerm() which takes n as input parameter and returns the nth term of the series.
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)
Constraints:
1<= n <=6000
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

def nth_term(n):
    c = 0
    prev = 0
    for i in range(2, int(100000.0)):
        if is_prime(i):
            prev = i
            c += 1
        if c == n:
            return prev * n + n