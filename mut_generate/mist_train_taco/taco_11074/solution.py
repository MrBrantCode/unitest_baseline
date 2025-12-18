"""
QUESTION:
A dragon symbolizes wisdom, power and wealth. On Lunar New Year's Day, people model a dragon with bamboo strips and clothes, raise them with rods, and hold the rods high and low to resemble a flying dragon.

A performer holding the rod low is represented by a 1, while one holding it high is represented by a 2. Thus, the line of performers can be represented by a sequence a1, a2, ..., an.

Little Tommy is among them. He would like to choose an interval [l, r] (1 ≤ l ≤ r ≤ n), then reverse al, al + 1, ..., ar so that the length of the longest non-decreasing subsequence of the new sequence is maximum.

A non-decreasing subsequence is a sequence of indices p1, p2, ..., pk, such that p1 < p2 < ... < pk and ap1 ≤ ap2 ≤ ... ≤ apk. The length of the subsequence is k.

Input

The first line contains an integer n (1 ≤ n ≤ 2000), denoting the length of the original sequence.

The second line contains n space-separated integers, describing the original sequence a1, a2, ..., an (1 ≤ ai ≤ 2, i = 1, 2, ..., n).

Output

Print a single integer, which means the maximum possible length of the longest non-decreasing subsequence of the new sequence.

Examples

Input

4
1 2 1 2


Output

4


Input

10
1 1 2 2 2 1 1 2 2 1


Output

9

Note

In the first example, after reversing [2, 3], the array will become [1, 1, 2, 2], where the length of the longest non-decreasing subsequence is 4.

In the second example, after reversing [3, 7], the array will become [1, 1, 1, 1, 2, 2, 2, 2, 2, 1], where the length of the longest non-decreasing subsequence is 9.
"""

def max_non_decreasing_subsequence_length(n, A):
    one = [0]
    two = [0]
    for i in A:
        one.append(one[-1])
        two.append(two[-1])
        if i == 1:
            one[-1] += 1
        else:
            two[-1] += 1
    
    rdp1 = [[1] * n for _ in range(n)]
    rdp2 = [[1] * n for _ in range(n)]
    
    for l in range(n):
        for r in range(l + 1, n):
            if A[r] == 2:
                rdp1[l][r] = rdp1[l][r - 1] + 1
            elif rdp1[l][r - 1] == one[r] - one[l]:
                rdp1[l][r] = rdp1[l][r - 1] + 1
            else:
                rdp1[l][r] = rdp1[l][r - 1]
            
            if A[r] == 1:
                rdp2[l][r] = rdp2[l][r - 1] + 1
            elif rdp2[l][r - 1] == two[r] - two[l]:
                rdp2[l][r] = rdp2[l][r - 1] + 1
            else:
                rdp2[l][r] = rdp2[l][r - 1]
    
    dp = [0] * n
    dp[0] = 1
    
    for i in range(1, n):
        if A[i] == 2:
            dp[i] = dp[i - 1] + 1
        elif dp[i - 1] == one[i]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
        
        dp[i] = max(dp[i], rdp2[0][i])
        
        for j in range(i):
            if rdp1[0][j] == one[j + 1]:
                dp[i] = max(dp[i], rdp1[0][j] + rdp2[j + 1][i])
            dp[i] = max(dp[i], rdp1[0][j] + two[i + 1] - two[j + 1])
    
    return dp[-1]