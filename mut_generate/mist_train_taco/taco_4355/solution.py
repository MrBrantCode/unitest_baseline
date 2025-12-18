"""
QUESTION:
You are given two numbers N and K and a set X.

X = { x : x is a natural number ≤ N } 
You have to find the total number of pairs of elements X[i] and X[j] belonging to the given set, such that,  i < j and their sum is divisible by K.

Input Format: 

An integer T followed by T lines, each containing a pair of space separated integers N and K.

Output Format: 

T integers on separate lines. Each integer denotes the answer corresponding to that test case.

Constraints: 

1≤T≤100 

K≤N≤10^9 

1≤K≤10000

SAMPLE INPUT
2
10 4
7 3

SAMPLE OUTPUT
10
7

Explanation

For the 1st test case, there are 10 pairs whose sum is divisible by 4. 
(1,3), (1,7), (2,6), (2,10), (3,5), (3,9), (4,8), (5,7), (6,10) and (7,9)

For the 2nd test case, there are 7 pairs whose sum is divisible by 3. 
(1,2), (1,5), (2,4), (2,7), (3,6), (4,5) and (5,7)
Register for IndiaHacks
"""

def count_divisible_pairs(N, K):
    total = 0
    a = N // K + 1
    b = (2 * N) // K - (1 if (2 * N) % K == 0 else 0)
    
    if K % 2 == 0:
        total += K * b * (b + 1) // 4 - b
    else:
        if b % 2 == 0:
            total += K * b * (b + 2) // 8 - b // 2
            total += K * b * (b + 2) // 8 - b * (K + 1) // 4
        else:
            total += K * (b - 1) * (b + 1) // 8 - (b - 1) // 2
            total += K * (b + 1) * (b + 3) // 8 - (b + 1) * (K + 1) // 4
    
    total -= (b - a + 1) * ((a + b) * K - 2 * (N + 1)) // 2
    
    return total