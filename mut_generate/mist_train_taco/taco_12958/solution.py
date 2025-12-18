"""
QUESTION:
One day John had to take care of his little nephew Jim. He was very busy, so he gave Jim a big bag full of building bricks. The bricks are of various heights: at most 15 different heights. For each height, the bag contains infinitely many bricks. 

Now, Jim’s task is to build every possible tower of height $N$ from the given bricks. Bricks are stacked vertically only and stand in an upright position. Two towers are different if their brick height sequences are different.

Jim is good at building towers and can build one tower in exactly 2 minutes, regardless of its height. John wants to know the time Jim requires to build all possible towers.  

Input Format 

There are $3$ lines of input. First line contains an integer, $N$, the height of tower to be built. Second line contains another integer, $\mbox{K}$, which represents different heights of bricks available in the bag. Third line contains $\mbox{K}$ distinct integers representing the available heights.  

Output Format 

In one line print the number of minutes Jim requires to build all possible towers. As this number can be very large, print the number modulo $(10^9+7)$.  

Constraints 

$1\leq N\leq10^{18}$ 

$1\leq K\leq15$ 

All heights will be unique. 

Height of each brick will lie in range [1, 15].  

Sample Input#00

10
1
1

Sample Output#00  

2

Explanation#00:  There is exactly one type of brick, so there is exactly one tower of height 10. Building any tower takes 2 minutes, so the answer is 2.

Sample Input#01  

5
2
2 3

Sample Output#01  

4

Explanation #01: There are two types of bricks. There are two different towers of height 5 which can be build from these types of bricks: $[2,3]$ and $[3,2]$. They are different, because the sequence of bricks in them is different. Building any tower takes 2 minutes, so the answer is $2\times2=4$.

Sample Input#03  

19
2
4 5

Sample Output#03

8

Explanation #03: There are two types of bricks. Jim can build 4 different towers of height $19$ from these bricks: $[5,5,5,4]$, $[5,5,4,5]$, $[5,4,5,5]$ and $[4,5,5,5]$. Building any tower takes 2 minutes, so the answer is $2\times4=8$.
"""

MOD = 10 ** 9 + 7

def mul(A, B):
    return [[sum([A[i][k] * B[k][j] for k in range(len(A[0]))]) % MOD for j in range(len(B[0]))] for i in range(len(A))]

def pow(A, e):
    P = [[1 if i == j else 0 for j in range(len(A[0]))] for i in range(len(A))]
    while e > 0:
        if e & 1:
            P = mul(P, A)
        A = mul(A, A)
        e >>= 1
    return P

def calculate_building_time(N, K, heights):
    A = [[1 if j == i + 1 else 0 for j in range(16)] for i in range(16)]
    for k in heights:
        A[k - 1][0] = 1
    P = pow(A, N)
    return 2 * P[0][0] % MOD