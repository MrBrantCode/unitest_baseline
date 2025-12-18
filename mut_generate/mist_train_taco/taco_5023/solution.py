"""
QUESTION:
Meera bought a house on Mars, and plans to decorate it with chains of alien flowers. Each flower is either red ($\mbox{R}$) or blue ($\mbox{B}$), and Meera knows how many occurrences of RR, RB, BB, and BR she wants to see in a chain.     

The diagram below shows a flower chain of length $10$:

In this example, RR occurs $2$ times (at positions ${0}$ and ${4}$), RB occurs $3$ times (at positions $1$, $5$, and $7$), BB occurs ${1}$ time (at position $2$), and BR occurs $3$ times (at positions $3$, ${6}$, and $8$).

Meera wants your help determining how many different chains with positive length can be made. Given $A,B,C$, and $\mbox{D}$, find the number of different chains having occurrences of RR, RB, BB and BR equal to inputs $A,B,C$, and $\mbox{D}$, respectively. As the answer can be very large, your printed output should be ${answer}\%(10^9+7)$.

Input Format

One line of space-separated, non-negative integers: $\mbox{A}$ (occurrences of RR), $\mbox{B}$ (occurrences of RB), $\mbox{C}$ (occurrences of BB), and $\mbox{D}$ (occurrences of BR), respectively.

Constraints

For $20\%$ Points: ${0}\leq A,B,C,D\leq4$

For $50\%$ Points: $0\leq A,B,C,D\leq10^2$

For ${100%}$ Points: $0\leq A,B,C,D\leq10^5$

Output Format

Find the number of chains having $A,B,C$, and $\mbox{D}$ occurrences of RR, RB, BB, and BR, respectively, and print the $\textit{answer}\%
 (10^9+7)$.

Sample Input
1 1 2 1

Sample Output
5

Explanation

The $5$ flower chains having exactly $1,1,2$, and ${1}$ occurrences of RR, RB, BB and BR are:
"""

P = 1000000007

def facmod(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
        r %= P
    return r

def invmod(n):
    return pow(n, P - 2, P)

def binmod(n, k):
    return facmod(n) * invmod(facmod(k) * facmod(n - k) % P) % P

def chose(n, k):
    return binmod(n + k - 1, k - 1)

def count_flower_chains(A, B, C, D):
    res = 0
    if B == 0 and D == 0:
        if A != 0 and C != 0:
            res = 0
        elif A == 0 and C == 0:
            res = 2
        else:
            res = 1
    elif B == D:
        res = chose(A, B) * chose(C, B + 1) + chose(A, B + 1) * chose(C, B)
    elif B - D == 1:
        res = chose(A, B) * chose(C, B)
    elif D - B == 1:
        res = chose(A, D) * chose(C, D)
    else:
        res = 0
    return res % P