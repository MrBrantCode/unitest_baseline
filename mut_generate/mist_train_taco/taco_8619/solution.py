"""
QUESTION:
Daruma Otoshi

You are playing a variant of a game called "Daruma Otoshi (Dharma Block Striking)".

At the start of a game, several wooden blocks of the same size but with varying weights are stacked on top of each other, forming a tower. Another block symbolizing Dharma is placed atop. You have a wooden hammer with its head thicker than the height of a block, but not twice that.

You can choose any two adjacent blocks, except Dharma on the top, differing at most 1 in their weight, and push both of them out of the stack with a single blow of your hammer. The blocks above the removed ones then fall straight down, without collapsing the tower. You cannot hit a block pair with weight difference of 2 or more, for that makes too hard to push out blocks while keeping the balance of the tower. There is no chance in hitting three blocks out at a time, for that would require superhuman accuracy.

The goal of the game is to remove as many blocks as you can. Your task is to decide the number of blocks that can be removed by repeating the blows in an optimal order.

<image>

Figure D1. Striking out two blocks at a time

In the above figure, with a stack of four blocks weighing 1, 2, 3, and 1, in this order from the bottom, you can hit middle two blocks, weighing 2 and 3, out from the stack. The blocks above will then fall down, and two blocks weighing 1 and the Dharma block will remain. You can then push out the remaining pair of weight-1 blocks after that.

Input

The input consists of multiple datasets. The number of datasets is at most 50. Each dataset is in the following format.

n
w1 w2 … wn


n is the number of blocks, except Dharma on the top. n is a positive integer not exceeding 300. wi gives the weight of the i-th block counted from the bottom. wi is an integer between 1 and 1000, inclusive.

The end of the input is indicated by a line containing a zero.

Output

For each dataset, output in a line the maximum number of blocks you can remove.

Sample Input


4
1 2 3 4
4
1 2 3 1
5
5 1 2 3 6
14
8 7 1 4 3 5 4 1 6 8 10 4 6 5
5
1 3 5 1 3
0


Output for the Sample Input


4
4
2
12
0






Example

Input

4
1 2 3 4
4
1 2 3 1
5
5 1 2 3 6
14
8 7 1 4 3 5 4 1 6 8 10 4 6 5
5
1 3 5 1 3
0


Output

4
4
2
12
0
"""

def max_removable_blocks(n, weights):
    if n == 0:
        return 0
    
    # Initialize a 2D list to check if blocks can be removed
    check = [[False] * n for _ in range(n)]
    
    # Check for adjacent blocks that can be removed
    for i in range(n - 1):
        if abs(weights[i + 1] - weights[i]) <= 1:
            check[i][i + 1] = True
    
    # Check for larger segments that can be removed
    for i in range(3, n, 2):
        for j in range(n - i):
            for k in range(j + 1, j + i):
                if not check[j][j + i] and check[j][k] and check[k + 1][j + i]:
                    check[j][j + i] = True
                    break
            if not check[j][j + i] and abs(weights[j] - weights[j + i]) <= 1 and check[j + 1][j + i - 1]:
                check[j][j + i] = True
    
    # Dynamic programming array to store the maximum removable blocks up to each index
    dp = [0] * (n + 1)
    
    # Fill the dp array
    for k in range(n):
        for m in range(k):
            if check[m][k]:
                dp[k] = max(dp[k], dp[m - 1] + k - m + 1)
        dp[k] = max(dp[k], dp[k - 1])
    
    return dp[n - 1]