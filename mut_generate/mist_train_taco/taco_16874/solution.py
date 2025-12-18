"""
QUESTION:
Read problems statements in Russian here 
Polo, the Penguin, has a lot of tests tomorrow at the university.
He knows that there are N different questions that will be on the tests. For each question i (i = 1..N), he knows C[i] - the number of tests that will contain this question, P[i] - the number of points that he will get for correctly answering this question on each of tests and T[i] - the amount of time (in minutes) that he needs to spend to learn this question.
Unfortunately, the amount of free time that Polo has is limited to W minutes. Help him to find the maximal possible total number of points he can get for all tests if he studies for no more than W minutes.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains the pair of integers N and W, separated by a space. The following N lines contain three space-separated integers C[i], P[i] and T[i] (i = 1..N).

------ Output ------ 

For each test case, output a single line containing the answer to the corresponding test case.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 100$
$1 ≤ C[i], P[i], T[i] ≤ 100
$$1 ≤ W ≤ 100$

----- Sample Input 1 ------ 
1
3 7
1 2 3
2 3 5
3 3 3
----- Sample Output 1 ------ 
11
----- explanation 1 ------ 
Example case 1. The best choice is to learn the first and the third questions and get 1*2 + 3*3 = 11 points.
"""

def calculate_maximal_points(T, test_cases):
    results = []
    for t in range(T):
        N, W, questions = test_cases[t]
        C = [q[0] for q in questions]
        P = [q[1] for q in questions]
        T = [q[2] for q in questions]
        
        dp = [[0 for j in range(W + 1)] for i in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if j < T[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - T[i - 1]] + C[i - 1] * P[i - 1])
        
        results.append(dp[N][W])
    
    return results