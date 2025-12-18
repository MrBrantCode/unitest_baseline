"""
QUESTION:
A cricket team consists of 11 players and some are good at batting, others are good at bowling and some of them are good at both batting and bowling. The batting coach wants to select exactly K players having maximum possible sum of scores. Given the batting score of each of the 11 players, find the number of ways in which we can select exactly K players such that the sum of their scores is the maximum possible. Two ways are different if there is a player who is selected in one of them is not in the other. See explanation of sample cases for more clarity.

------ Input ------ 

First line contains T, number of test cases ( 1 ≤ T ≤ 100 ). T cases follow, each having 2 lines. First line of each case contains scores of 11 players ( 1 ≤ score ≤ 100 ) and the second line contains K (1 ≤ K ≤ 11)

------ Output ------ 

For each test case, output the answer in a new line.

----- Sample Input 1 ------ 
2
1 2 3 4 5 6 7 8 9 10 11
3
2 5 1 2 4 1 6 5 2 2 1
6
----- Sample Output 1 ------ 
1
6
----- explanation 1 ------ 
Case 1 : Maximum possible sum of scores = 11 + 10 + 9 = 30 and can be achieved only by selecting the last 3 players. Only one possible way.
Case 2 : Maximum possible sum of scores = 6 + 5 + 5 + 4 + 2 + 2 = 24 and considering the players as p1 p2 p3 ... p11 in that order, the ones with maximum possible sum of scores is as follows
{p1, p2, p4, p5, p7, p8 }
{p10, p2, p4, p5, p7, p8 }
{p1, p2, p10, p5, p7, p8 }
{p9, p2, p4, p5, p7, p8 }
{p1, p2, p9, p5, p7, p8 }
{p10, p2, p9, p5, p7, p8 }
"""

import math

def max_batting_score_ways(scores, K):
    # Sort the scores in descending order
    scores.sort(reverse=True)
    
    # Get the K-th highest score
    k_th_highest_score = scores[K-1]
    
    # Count the number of players with the K-th highest score
    count_k_th_highest = scores.count(k_th_highest_score)
    
    # Count the number of players with the K-th highest score in the top K players
    count_in_top_k = 0
    for i in range(K):
        if scores[i] == k_th_highest_score:
            count_in_top_k += 1
    
    # Calculate the number of ways to choose the required number of players
    return math.comb(count_k_th_highest, count_in_top_k)