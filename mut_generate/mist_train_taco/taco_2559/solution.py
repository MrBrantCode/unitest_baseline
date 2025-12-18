"""
QUESTION:
Level 3 

Given an array a of size n containing only 0,-1,and 1,

x = number of 1's in a[l,r] (in subarray from l to r)

y = number of -1's in a[l,r] (in subarray from l to r)

For any sub array [l,r] function f is defined as follows

if(y == 0)

f([l,r]) = 0;

else

f([l,r]) = x / y;

Your goal is determine the maximum value of the function f.
Print the maximum value in most reduced fraction form i.e. p/q where gcd(p,q) = 1.

Input Format:

First line contains T, the number of test cases (1 ≤ T ≤ 10)

For each test case line,first line contains n, the size of array (1 ≤ n ≤ 10^5)

Second line of each test case contains n space separated integers. (a[i] /belongs to/ {-1,0,1})

Output Format:

Print maximum value of function f in reduced fraction form without any spaces for each test case in a single line

Author : Sumeet Varma

SAMPLE INPUT
2
2
1 1
3
1 1 -1

SAMPLE OUTPUT
0/1
2/1
"""

def max_f_value(arr, n):
    l = 0
    r = 0
    f = 0
    ma = 0
    
    for num in arr:
        if num == 1:
            r += 1
        elif num == -1:
            f = 1
            l = r
            r = 0
        if l + r > ma:
            ma = l + r
    
    if f == 0:
        return (0, 1)
    else:
        return (ma, 1)