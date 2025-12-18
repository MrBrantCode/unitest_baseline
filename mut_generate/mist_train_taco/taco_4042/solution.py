"""
QUESTION:
N different natural numbers are given. If you select four different ones and set them as $ A $, $ B $, $ C $, $ D $, the following formula

$ \ Frac {A + B} {C --D} $



I want to find the maximum value of.




Given N different natural numbers, choose 4 different from them and create a program to find the maximum value of the above formula.



Input

The input is given in the following format.


N
a1 a2 ... aN


The number N (4 ≤ N ≤ 1000) of natural numbers is given in the first line. The value ai (1 ≤ ai ≤ 108) of each natural number is given in the second line. However, the same natural number does not appear more than once (ai ≠ aj for i ≠ j).

Output

Outputs the maximum value of the above formula as a real number for a given N natural numbers. However, the error must not exceed plus or minus 10-5.

Examples

Input

10
1 2 3 4 5 6 7 8 9 10


Output

19.00000


Input

5
22 100 42 3 86


Output

9.78947


Input

6
15 21 36 10 34 5


Output

18.00000


Input

4
100000 99999 8 1


Output

28571.285714
"""

def find_max_value(n, a):
    a = sorted(a)
    b = [(a[i + 1] - a[i], i) for i in range(n - 1)]
    b.sort(key=lambda x: x[0])
    
    if b[0][1] < n - 2:
        return (a[-1] + a[-2]) / b[0][0]
    elif b[0][1] == n - 3:
        if b[1][1] == n - 2:
            return max((a[-1] + a[-2]) / b[2][0], (a[-1] + a[-4]) / b[0][0], (a[-3] + a[-4]) / b[1][0])
        else:
            return max((a[-1] + a[-2]) / b[1][0], (a[-1] + a[-4]) / b[0][0])
    elif b[1][1] == n - 3:
        return max((a[-1] + a[-2]) / b[2][0], (a[-1] + a[-4]) / b[1][0], (a[-3] + a[-4]) / b[0][0])
    else:
        return max((a[-1] + a[-2]) / b[1][0], (a[-3] + a[-4]) / b[0][0])