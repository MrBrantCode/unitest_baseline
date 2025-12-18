"""
QUESTION:
Manasa was sulking her way through a boring class when suddenly her teacher singled her out and asked her a question. He gave her a number n and Manasa has to come up with the smallest number m which contains atleast n number of zeros at the end of m!. Help Manasa come out of the sticky situation. 

Input Format 

The first line contains an integer T i.e. the number of Test cases. 

Next T lines will contain an integer n.  

Output Format 

Print smallest such number m. 

Constraints 

1 ≤ T ≤ 100 

1 ≤ n ≤ 10^{16}  

Sample Input  

3
1
2
3

Sample Output  

5
10
15

Explanation

As 4! = 24 and 5! = 120, so minimum value of m will be 5.
As 9! = 362880 and 10! = 3628800, so minimum value of m will be 10.
As 14! = 87178291200 and 15! = 1307674368000, so minimum value of m will be 15.
"""

from math import log, ceil

def invf(n):
    if n == 0:
        return 0
    return sum((n // 5 ** i for i in range(1, int(log(n, 5)) + 1)))

def bsearch(inv, y):
    lb = 1
    ub = y * 5
    while ub - lb > 1:
        mid = (ub + lb) // 2
        if inv(mid) >= y:
            ub = mid
        elif inv(mid) < y:
            lb = mid
    if inv(lb) == y:
        return lb
    else:
        return ub

def find_smallest_m(n):
    return bsearch(invf, n)