"""
QUESTION:
You are given integers N and K. Find the number of triples (a,b,c) of positive integers not greater than N such that a+b,b+c and c+a are all multiples of K.
The order of a,b,c does matter, and some of them can be the same.

-----Constraints-----
 - 1 \leq N,K \leq 2\times 10^5
 - N and K are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K

-----Output-----
Print the number of triples (a,b,c) of positive integers not greater than N such that a+b,b+c and c+a are all multiples of K.

-----Sample Input-----
3 2

-----Sample Output-----
9

(1,1,1),(1,1,3),(1,3,1),(1,3,3),(2,2,2),(3,1,1),(3,1,3),(3,3,1) and (3,3,3) satisfy the condition.
"""

def count_valid_triples(N, K):
    cnt1 = 0
    cnt2 = 0
    
    if K % 2 == 1:
        for i in range(1, N + 1):
            if i % K == 0:
                cnt1 += 1
        return cnt1 ** 3
    else:
        for i in range(1, N + 1):
            if i % K == K // 2:
                cnt2 += 1
            if i % K == 0:
                cnt1 += 1
        return cnt1 ** 3 + cnt2 ** 3