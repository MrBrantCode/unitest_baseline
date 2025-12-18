"""
QUESTION:
Two players (numbered $\mbox{1}$ and $2$) are playing a game of Tower Breakers! The rules of the game are as follows:

Player $\mbox{1}$ always moves first, and both players always move optimally.
Initially there are $N$ towers of various heights.
The players move in alternating turns. In each turn, a player can choose a tower of height $\mbox{X}$ and reduce its height to $\mathbf{Y}$, where $1\leq Y<X$ and $\mathbf{Y}$ evenly divides $\mbox{X}$.
If the current player is unable to make any move, they lose the game.

Given the value of $N$ and the respective height values for all towers, can you determine who will win? If the first player wins, print $\mbox{1}$; otherwise, print $2$.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of test cases. 

Each of the $2T$ subsequent lines defines a test case. Each test case is described over the following two lines:

An integer, $N$, denoting the number of towers.
$N$ space-separated integers, $h_0,h_1,\ldots,h_{N-1}$, where each $h_i$ describes the height of tower $\boldsymbol{i}$.

Constraints

$1\leq T\leq100$
$1\leq N\leq100$
$1\leq h_i\leq10^6$

Output Format

For each test case, print a single integer denoting the winner (i.e., either $\mbox{1}$ or $2$) on a new line.

Sample Input
2
2 
1 2
3 
1 2 3

Sample Output
1
2

Explanation

Test Case 0: 

Player $\mbox{1}$ reduces the second tower to height $\mbox{1}$ and subsequently wins.

Test Case 1: 

There are two possible moves:

Reduce the second tower to $\mbox{1}$ 
Reduce the third tower to $\mbox{1}$. 

Whichever move player $\mbox{1}$ makes, player $2$ will make the other move. Thus, player $2$ wins.
"""

def determine_winner(test_cases):
    def nim_sum(a):
        ans = 0
        for num in a:
            ans = ans ^ num
        return ans

    results = []
    
    for case in test_cases:
        N, heights = case
        b = [0] * N
        
        for i in range(N):
            if heights[i] == 1:
                b[i] = 0
            else:
                b[i] = 0
                j = 2
                root = int(pow(heights[i], 0.5))
                while heights[i] != 1 and j <= root:
                    if heights[i] % j == 0:
                        while heights[i] % j == 0:
                            b[i] += 1
                            heights[i] = heights[i] // j
                    j += 1
                if heights[i] != 1:
                    b[i] += 1
        
        ans = nim_sum(b)
        if ans != 0:
            results.append(1)
        else:
            results.append(2)
    
    return results