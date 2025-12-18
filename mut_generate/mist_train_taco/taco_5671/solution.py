"""
QUESTION:
Shil likes Round numbers very much . A  number is called Round number if its non-negative and its first and last digits are same. For example  0 , 3 , 343 and  50005 are round numbers whereas 1000 is not  a round number. Shil has  an array A1 , A2  .. AN . He wants to answer Q queries of following two type :
1 l r  : Find total number of round numbers in range [l, r]
2 i K  : Update i^th element of array A to K  i.e perform the  operation Ai = K. 
Since you are the friend of Shil , he asks for your help .

INPUT:
First line consists of two integers N and Q. Next line consists of N integers A1 , A2  .. AN. Next line consists of Q queries. Each query consists of three integers as mentioned in the problem.

OUTPUT: 
For each query of type 2 , output total number of round numbers in range [l,r].

CONSTRAINTS:
1 ≤ N , Q ≤ 2*10^5
-10^18 ≤ Ai ≤ 10^18 
1 ≤ l,r ≤ N
-10^18 ≤ K ≤ 10^18

SAMPLE INPUT
5 5 
1 2 33 456 111
1 1 2
1 1 5
2 1 6
2 2 1000
1 1 5

SAMPLE OUTPUT
2
4
3

Explanation

Out of all the initial numbers given in array A :- 1,2,33,111 are round numbers .
For 1^st query , there are two round numbers - A[1] and A[2].
For 2^st query , there are 4 round numbers - A[1] , A[2] , A[3] , A[5].
In   3^rd query , we are updating 1st position with 6 , which is a round number.
In   4^th query , we are updating 2nd position with 1000 , which isn't a round number.  
For 5^th query , there are 3 round numbers - A[1] , A[3] and  A[5].
"""

def process_round_number_queries(N, Q, A, queries):
    def is_round_number(num):
        s = str(num)
        return s[0] == s[-1]

    def update(x, v):
        while x <= N:
            bit[x] += v
            x += x & -x

    def query(x):
        total = 0
        while x > 0:
            total += bit[x]
            x -= x & -x
        return total

    bit = [0] * (N + 1)
    X = [is_round_number(A[i]) for i in range(N)]

    for i in range(N):
        if X[i]:
            update(i + 1, 1)

    results = []
    for q in queries:
        a, b, c = q
        if a == 1:
            l, r = b, c
            results.append(query(r) - query(l - 1))
        elif a == 2:
            i, K = b, c
            new = is_round_number(K)
            if X[i - 1] != new:
                X[i - 1] = new
                if new:
                    update(i, 1)
                else:
                    update(i, -1)

    return results