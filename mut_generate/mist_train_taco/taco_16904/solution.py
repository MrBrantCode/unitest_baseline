"""
QUESTION:
Chef has N subordinates. In order to complete a very important order he will choose exactly K of them. He can't choose less than K since it will be not enough to complete the order in time. On the other hand if he chooses more than K subordinates he can't control them during the operation. Help him to find the number of ways he can choose the team to complete this very important order.

------ Input ------ 

The first line contains a single positive integer T ≤ 100, the number of test cases. T test cases follow. The only line of each test case contains two integers N and K, where 0 ≤ N, K < 2^{64}. It is guaranteed that the answer will be less than 2^{64}.

------ Output ------ 

For each test case, output a single line containing the number of ways to choose the required team.

----- Sample Input 1 ------ 
3
2 1
3 3
10 5
----- Sample Output 1 ------ 
2
1
252
"""

def calculate_team_combinations(n, k):
    """
    Calculate the number of ways to choose k subordinates from n subordinates.

    Parameters:
    n (int): The total number of subordinates.
    k (int): The number of subordinates to choose.

    Returns:
    int: The number of ways to choose the required team.
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0