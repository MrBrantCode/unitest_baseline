"""
QUESTION:
A thief sneaked into a museum with a lot of treasures with only one large furoshiki. There are many things I want to steal, but the weight that the furoshiki can withstand is limited, and if it exceeds this, the furoshiki will tear. Therefore, the thief must consider a combination of treasures that will not break the prepared furoshiki and will be the most valuable.

The weight W that the bath room can withstand, and the value and weight of each treasure in the museum are read, and the total value of the treasure is the maximum when the total value does not exceed W. Create a program that outputs the total weight. However, if there are multiple combinations that maximize the sum of values, the one with the smallest sum of weights will be output.



Input

Given multiple datasets. Each dataset is given in the following format:


W
N
v1, w1
v2, w2
::
vN, wN


The first line gives the integer W (W ≤ 1,000), which represents the weight that the furoshiki can bear, and the second line gives the number of treasures N (1 ≤ N ≤ 1,000). The next N lines are given a set of the integer vi (0 ≤ vi ≤ 10,000) representing the value of the i-th treasure and the integer wi (0 ≤ wi ≤ W) representing its weight.

When W is 0, it is the last input. The number of datasets does not exceed 50.

Output

Output as follows for each data set.


Case dataset number:
Sum of the value of the treasure in the furoshiki
Sum of the weight of the treasure at that time


Example

Input

50
5
60,10
100,20
120,30
210,45
10,4
50
5
60,10
100,20
120,30
210,45
10,4
0


Output

Case 1:
220
49
Case 2:
220
49
"""

def find_optimal_treasure_combination(W, treasures):
    n = len(treasures)
    dp = [0] * (W + 1)
    
    for value, weight in treasures:
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
    
    max_value = dp[W]
    min_weight = W
    
    for j in range(W + 1):
        if dp[j] == max_value:
            min_weight = min(min_weight, j)
    
    return max_value, min_weight