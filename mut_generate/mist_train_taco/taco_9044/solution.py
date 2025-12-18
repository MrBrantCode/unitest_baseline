"""
QUESTION:
Our unsung tower-breaking heroes (players $\mathbf{P_1}$ and $P_2$) only have one tower left, and they've decided to break it for a special game commemorating the end of $5$ days of Game Theory! The rules are as follows:

$\mathbf{P_1}$ always moves first, and both players always move optimally.
Initially there is $\mbox{1}$ tower of height $N$.
The players move in alternating turns. The moves performed by each player are different:
At each turn, $\mathbf{P_1}$ divides the current tower into some number of smaller towers. If the turn starts with a tower of height $\mbox{H}$ and $\mathbf{P_1}$ breaks it into $x\geq2$ smaller towers, the following condition must apply: $H=h_1+h_2+...+h_x$, where $h_i$ denotes the height of the $i^{\mbox{th}}$ new tower.
At each turn, $P_2$ chooses some tower $\boldsymbol{\mbox{k}}$ of the $\boldsymbol{x}$ new towers made by $\mathbf{P_1}$ (where $1\leq k\leq x$). Then $\mathbf{P_1}$ must pay $k^2$ coins to $P_2$. After that, $\mathbf{P_1}$ gets another turn with tower $h_{k}$ and the game continues.
The game is over when no valid move can be made by $\mathbf{P_1}$, meaning that $H=1$.
$\mathbf{P_1}$'s goal is to pay as few coins as possible, and $P_2$'s goal is to earn as many coins as possible. 

Can you predict the number of coins that $P_2$ will earn?

Input Format

The first line contains a single integer, $\mathbf{T}$, denoting the number of test cases. 

Each of the $\mathbf{T}$ subsequent lines contains a single integer, $N$, defining the initial tower height for a test case.

Constraints

$1\leq T\leq100$
$2\leq N\leq10^{18}$

Output Format

For each test case, print a single integer denoting the number of coins earned by $P_2$ on a new line.

Sample Input
3
4
2
7

Sample Output
6
4
8

Explanation

Test Case 0: 

Our players make the following moves:

$H=N=4$
$\mathbf{P_1}$ splits the initial tower into $2$ smaller towers of sizes $3$ and $\mbox{1}$. 
$P_2$ chooses the first tower and earns $1^2=1$ coin. 
$H=3$
$\mathbf{P_1}$ splits the tower into $2$ smaller towers of sizes $2$ and $\mbox{1}$. 
$P_2$ chooses the first tower and earns $1^2=1$ coin.
$H=2$
$\mathbf{P_1}$ splits the tower into $2$ smaller towers of size $\mbox{1}$. 
$P_2$ chooses the second tower and earns $2^2=4$ coins.

The total number of coins earned by $P_2$ is $1+1+4=6$, so we print $\boldsymbol{6}$ on a new line.
"""

def calculate_coins_earned(T, N):
    largest = 1000000000000000000
    height = [0] * 1000
    height[0] = 1
    
    for i in range(1, 261):
        for j in range(1, int(i ** 0.5) + 1):
            height[i] += height[i - j * j]
            if height[i] > largest:
                break
    
    results = []
    for n in N:
        for i in range(261):
            if height[i] >= n:
                results.append(i)
                break
    
    return results