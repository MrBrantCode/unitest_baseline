"""
QUESTION:
In a tournament, $n$ players play against each other exactly once. Each game results in exactly one player winning. There are no ties. You have been given a scorecard containing the scores of each player at the end of the tournament. The score of a player is the total number of games the player won in the tournament. However, the scores of some players might have been erased from the scorecard. How many possible scorecards are consistent with the input scorecard?

Input Format

The first line contains a single integer $\boldsymbol{\boldsymbol{t}}$ denoting the number of test cases. $\boldsymbol{\boldsymbol{t}}$ test cases follow.  

The first line of each test case contains a single integer $n$. The second line contains $n$ space-separated integers $s_1,s_2,\ldots,s_n$. $s_i$ denotes the score of the $\boldsymbol{i}$th player. If the score of the $\boldsymbol{i}$th player has been erased, it is represented by $-1$.

Constraints

$1\leq t\leq20$
$1\leq n\leq40$
$-1\leq s_i<n$

Output Format

For each test case, output a single line containing the answer for that test case modulo $10^9+7$. 

Sample Input 0
5
3
-1 -1 2
3
-1 -1 -1
4
0 1 2 3
2
1 1
4
-1 -1 -1 2

Sample Output 0
2
7
1
0
12

Explanation 0

For the first case, there are 2 scorecards possible: (0,1,2) or (1,0,2). 

For the second case, the valid scorecards are (1,1,1), (0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0). 

For the third case, the only valid scorecard is (0,1,2,3). 

For the fourth case, there is no valid scorecard. It is not possible for both players to have score of 1. 

For the fifth case, 6-variations of {(3,1,0)[2]}, and 3 variations each of {(2,2,0)[2]} and {(2,1,1)[2]}.
"""

MOD = 10**9 + 7

def binom(n, r):
    if r < 0 or n < r:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return n * binom(n - 1, r - 1) // r

def count_possible_scorecards(n, scores):
    # Filter out the erased scores and calculate the sum of known scores
    known_scores = [score for score in scores if score != -1]
    known_sum = sum(known_scores)
    
    # Check if the known scores are valid
    if known_sum > n * (n - 1) // 2 or known_scores.count(0) > 1:
        return 0
    
    # If all scores are known and valid, there is only one possible scorecard
    if len(known_scores) == n:
        return 1
    
    # Calculate the number of erased scores and the remaining sum needed
    erased_count = n - len(known_scores)
    remaining_sum = n * (n - 1) // 2 - known_sum
    
    # Calculate the number of possible scorecards
    result = binom(remaining_sum - 1, remaining_sum - erased_count)
    if 0 not in known_scores:
        result += erased_count * binom(remaining_sum - 1, remaining_sum - erased_count + 1)
    
    return result % MOD