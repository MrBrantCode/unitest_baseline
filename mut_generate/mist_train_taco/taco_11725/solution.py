"""
QUESTION:
My futon

You bought N futons in preparation for your new life. The i-th futon has the warmth supply capacity of si. From the temperature forecast for the next M days, the warmth demand of dj is expected on the jth day. If the warmth is not enough or too much, the comfort will be impaired, so the absolute value of the difference between the sum of the warmth supply capacity of the futon on the j day and the dj is called the discomfort on the j day. To do. I want to make the total discomfort for M days as small as possible.

By the way, your room is unfortunately very small, with only a bed and a closet. Therefore, the only way to add one futon to the bed is to put the futon at the top of the closet on the top of the bed. Conversely, the only way to reduce one bed futon is to put the futon at the top of the bed at the top of the closet. There is no limit to the number of futons that can be moved per day, but only one can be moved at a time.

By the way, you plan to put the futon you bought in the closet. Only at this time can the futons be put in the closet in any order. How do you store your futon in the closet, and then how do you put it in and out every day so that you can spend your days comfortably? When minimizing the sum of discomfort for M days, find the value of that sum. There may be futons that have never been used, and there may be days when no futons are used.

Input

The input consists of multiple datasets. Each dataset has the following format.

> N M
> s1 s2 ... sN
> d1 d2 ... dM

The first line of the dataset is given an integer representing the number of futons N and the number of days M for which the temperature is predicted, separated by spaces. On the second line, N integers s1, s2, ..., sN are given separated by spaces, and si represents the warmth supply capacity of the i-th futon. On the third line, M integers d1, d2, ..., dM are given separated by spaces, and dj represents the warmth demand on day j. These integers satisfy 1 ≤ N ≤ 15, 1 ≤ M ≤ 100, 1 ≤ si, dj ≤ 1,000,000.

The end of the input is represented by a dataset of N = M = 0. Do not output for this dataset.

Output

For each dataset, output the minimum sum of discomfort for M days on one line.

Sample Input


1 1
Five
6
1 1
Five
2
1 1
20
Five
4 1
2 4 5 9
8
4 3
3 5 2 1
10 4 7
5 5
2 2 2 2 2
1 3 5 7 9
twenty five
twenty five
2 5 2 5 2
0 0

Output for Sample Input


1
2
Five
1
1
Five
Four


For the 5th case, put it in the closet with 5, 2, 3, 1 from the top, and take out 3 sheets on the 1st day | 10-(5 + 2 + 3) | = 0, 2 sheets on the 2nd day | 4 -5 | = Take out one sheet on the 1st and 3rd days | 7-(5 + 2) | = 0, for a total of 0 + 1 + 0 = 1.





Example

Input

1 1
5
6
1 1
5
2
1 1
20
5
4 1
2 4 5 9
8
4 3
3 5 2 1
10 4 7
5 5
2 2 2 2 2
1 3 5 7 9
2 5
2 5
2 5 2 5 2
0 0


Output

1
2
5
1
1
5
4
"""

def minimize_discomfort(N, M, S, D):
    if N == 0 or M == 0:
        return 0
    
    S.sort()
    D.sort()
    SA = sum(S)
    rest = sum((d - SA for d in D if SA <= d))
    memo = {2 ** N - 1: rest}

    def dfs(state, su, idx):
        if state in memo:
            return memo[state]
        res = 10 ** 18
        for i in range(N):
            if state >> i & 1 == 0:
                s = 0
                j = idx
                nxt = su + S[i]
                while j < M and D[j] <= nxt:
                    s += min(nxt - D[j], D[j] - su)
                    j += 1
                res = min(res, s + dfs(state | 1 << i, su + S[i], j))
        memo[state] = res
        return res
    
    return dfs(0, 0, 0)