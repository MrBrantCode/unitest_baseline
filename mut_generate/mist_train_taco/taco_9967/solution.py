"""
QUESTION:
Problem statement

A $ 2 $ human-player match-up game tournament is about to take place in front of Kyoto University Camphor Tree.

There are $ 2 ^ N $ participants in this tournament, numbered from $ 1 $ to $ 2 ^ N $.

Winning or losing when $ 2 $ of participants fight is represented by the $ 2 ^ N-1 $ string $ S $ consisting of $ 0 $ and $ 1 $.

When people $ x $ and people $ y $$ (1 \ le x <y \ le 2 ^ N) $ fight

* When $ S_ {y-x} = 0 $, the person $ x $ wins,
* When $ S_ {y-x} = 1 $, the person $ y $ wins



I know that.

The tournament begins with a line of participants and proceeds as follows:

1. Make a pair of $ 2 $ people from the beginning of the column. For every pair, $ 2 $ people in the pair fight.
2. Those who win the match in 1 will remain in the line, and those who lose will leave the line.
3. If there are more than $ 2 $ left, fill the column back to 1.
4. If there are $ 1 $ left, that person will be the winner.



Now, the participants are initially arranged so that the $ i $ th $ (1 \ le i \ le 2 ^ N) $ from the beginning becomes the person $ P_i $.

Solve the following problem for all integers $ k $ that satisfy $ 0 \ le k \ le 2 ^ N-1 $.

* From the initial state, the first $ k $ person moves to the end of the column without changing the order.
* In other words, if you list the number of participants in the moved column from the beginning, $ P_ {k + 1}, P_ {k + 2}, ..., P_ {2 ^ N}, P_1, P_2, ..., P_k $.
* Find the winner's number when you start the tournament from the line after the move.



Constraint

* $ 1 \ leq N \ leq 18 $
* $ N $ is an integer.
* $ S $ is a $ 2 ^ N-1 $ string consisting of $ 0 $ and $ 1 $.
* $ P $ is a permutation of integers from $ 1 $ to $ 2 ^ N $.



* * *

input

Input is given from standard input in the following format.


$ N $
$ S_1S_2 \ ldots S_ {2 ^ N-1} $
$ P_1 $ $ P_2 $ $ \ ldots $ $ P_ {2 ^ N} $


output

Output $ 2 ^ N $ lines.

In the $ i $ line $ (1 \ le i \ le 2 ^ N) $, output the answer to the above problem when $ k = i-1 $.

* * *

Input example 1


2
100
1 4 2 3


Output example 1


1
2
1
2


For example, if $ k = 2 $, the number of participants in the moved column will be $ 2, 3, 1, 4 $ from the beginning.

When person $ 2 $ and person $ 3 $ fight, person $ 3 $ wins over $ S_1 = 1 $.

When person $ 1 $ and person $ 4 $ fight, person $ 1 $ wins over $ S_3 = 0 $.

When person $ 3 $ and person $ 1 $ fight, person $ 1 $ wins over $ S_2 = 0 $.

Therefore, if $ k = 2 $, the winner would be $ 1 $ person.

* * *

Input example 2


Four
101011100101000
8 15 2 9 12 5 1 7 14 10 11 3 4 6 16 13


Output example 2


16
1
16
2
16
12
Ten
14
16
1
16
2
16
12
Ten
14


* * *

Input example 3


1
0
1 2


Output example 3


1
1






Example

Input

2
100
1 4 2 3


Output

1
2
1
2
"""

def find_tournament_winner(N, S, P):
    def f(a, b):
        return max(a, b) if S[abs(a - b) - 1] == '1' else min(a, b)
    
    dp = [[0 if j else P[i] for j in range(N + 1)] for i in range(1 << N)]
    maxn = 1 << N
    
    for j in range(N):
        j1 = 1 << j
        for i in range(1 << N):
            if i + j1 >= maxn:
                dp[i][j + 1] = f(dp[i][j], dp[i + j1 - maxn][j])
            else:
                dp[i][j + 1] = f(dp[i][j], dp[i + j1][j])
    
    return [dp[i][-1] for i in range(1 << N)]