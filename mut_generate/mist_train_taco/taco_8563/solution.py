"""
QUESTION:
Gaius Julius Caesar, a famous general, loved to line up his soldiers. Overall the army had n1 footmen and n2 horsemen. Caesar thought that an arrangement is not beautiful if somewhere in the line there are strictly more that k1 footmen standing successively one after another, or there are strictly more than k2 horsemen standing successively one after another. Find the number of beautiful arrangements of the soldiers. 

Note that all n1 + n2 warriors should be present at each arrangement. All footmen are considered indistinguishable among themselves. Similarly, all horsemen are considered indistinguishable among themselves.

Input

The only line contains four space-separated integers n1, n2, k1, k2 (1 ≤ n1, n2 ≤ 100, 1 ≤ k1, k2 ≤ 10) which represent how many footmen and horsemen there are and the largest acceptable number of footmen and horsemen standing in succession, correspondingly.

Output

Print the number of beautiful arrangements of the army modulo 100000000 (108). That is, print the number of such ways to line up the soldiers, that no more than k1 footmen stand successively, and no more than k2 horsemen stand successively.

Examples

Input

2 1 1 10


Output

1


Input

2 3 1 2


Output

5


Input

2 4 1 1


Output

0

Note

Let's mark a footman as 1, and a horseman as 2.

In the first sample the only beautiful line-up is: 121

In the second sample 5 beautiful line-ups exist: 12122, 12212, 21212, 21221, 22121
"""

def count_beautiful_arrangements(n1, n2, k1, k2):
    # Adjust k1 and k2 to be within the bounds of n1 and n2 respectively
    k1 = min(k1, n1)
    k2 = min(k2, n2)
    
    # Initialize the DP table
    dp = [[[0] * 2 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    
    # Base cases
    for i in range(k1 + 1):
        dp[i][0][0] = 1
    for i in range(k2 + 1):
        dp[0][i][1] = 1
    
    # Fill the DP table
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            dp[i][j][0] = sum((dp[k][j][1] for k in range(max(0, i - k1), i))) % 100000000
            dp[i][j][1] = sum((dp[i][k][0] for k in range(max(0, j - k2), j))) % 100000000
    
    # Return the result
    return sum(dp[n1][n2]) % 100000000