"""
QUESTION:
Taro and Jiro will play the following game against each other.

Initially, they are given a sequence a = (a_1, a_2, \ldots, a_N). Until a becomes empty, the two players perform the following operation alternately, starting from Taro:

* Remove the element at the beginning or the end of a. The player earns x points, where x is the removed element.



Let X and Y be Taro's and Jiro's total score at the end of the game, respectively. Taro tries to maximize X - Y, while Jiro tries to minimize X - Y.

Assuming that the two players play optimally, find the resulting value of X - Y.

Constraints

* All values in input are integers.
* 1 \leq N \leq 3000
* 1 \leq a_i \leq 10^9

Input

Input is given from Standard Input in the following format:


N
a_1 a_2 \ldots a_N


Output

Print the resulting value of X - Y, assuming that the two players play optimally.

Examples

Input

4
10 80 90 30


Output

10


Input

3
10 100 10


Output

-80


Input

1
10


Output

10


Input

10
1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1


Output

4999999995


Input

6
4 2 9 7 1 5


Output

2
"""

def optimal_game_score_difference(a: list[int]) -> int:
    N = len(a)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    
    # Initialize the diagonal of the dp table
    for i in range(N):
        dp[i][i] = a[i]
    
    # Fill the dp table
    for i in range(N - 1, -1, -1):
        for j in range(i, N):
            if dp[i][j] != -1:
                continue
            dp[i][j] = max(a[i] - dp[i + 1][j], a[j] - dp[i][j - 1])
    
    return dp[0][-1]