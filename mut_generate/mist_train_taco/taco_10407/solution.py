"""
QUESTION:
There are N problems numbered 1..N which you need to complete. You've arranged the problems in increasing difficulty order, and the i^{th} problem has estimated difficulty level i. You have also assigned a rating vi to each problem. Problems with similar vi values are similar in nature. On each day, you will choose a subset of the problems and solve them. You've decided that each subsequent problem solved on the day should be tougher than the previous problem you solved on that day. Also, to make it less boring, consecutive problems you solve should differ in their vi rating by at least K. What is the least number of days in which you can solve all problems?

Input Format

The first line contains the number of test cases T. T test cases follow. Each case contains an integer N and K on the first line, followed by integers v1,...,vn on the second line.

Constraints

1 <= T <= 100 

1 <= N <= 300 

1 <= vi <= 1000 

1 <= K <= 1000

Output Format

Output T lines, one for each test case, containing the minimum number of days in which all problems can be solved.

Sample Input
2  
3 2  
5 4 7  
5 1  
5 3 4 5 6

Sample Output
2  
1

Explanation

For the first example, you can solve the problems with rating 5 and 7 on the first day and the problem with rating 4 on the next day. Note that the problems with rating 5 and 4 cannot be completed consecutively because the ratings should differ by at least K (which is 2). Also, the problems cannot be completed in order 5,7,4 in one day because the problems solved on a day should be in increasing difficulty level.

For the second example, all problems can be solved on the same day.
"""

def minimum_days_to_solve_problems(test_cases):
    def find(v):
        for u in G[v]:
            if not V[u]:
                V[u] = True
                if M[u] == -1 or find(M[u]):
                    M[u] = v
                    return True
        return False

    results = []
    for case in test_cases:
        n, k, vi = case
        G = [[] for _ in range(n)]
        V = [False for _ in range(n)]
        M = [-1 for _ in range(n)]
        
        for x in range(n):
            for y in range(x + 1, n):
                if abs(vi[x] - vi[y]) >= k:
                    G[x].append(y)
        
        res = 0
        for i in range(n):
            V = [False for _ in range(n)]
            if find(i):
                res += 1
        
        results.append(n - res)
    
    return results