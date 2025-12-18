"""
QUESTION:
Two people are playing Nimble! The rules of the game are:

The game is played on a line of $n$ squares, indexed from $\mbox{0}$ to $n-1$. Each square $\boldsymbol{i}$ (where $0\leq i<n$) contains $c_i$ coins. For example: 

The players move in alternating turns. During each move, the current player must  remove exactly $\mbox{1}$ coin from square $\boldsymbol{i}$ and move it to square $j$ if and only if $0\leq j<i$.
The game ends when all coins are in square $\mbox{0}$ and nobody can make a move. The first player to have no available move loses the game.

Given the value of $n$ and the number of coins in each square, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of test cases. 

Each of the $2T$ subsequent lines defines a test case. Each test case is described over the following two lines:

An integer, $n$, denoting the number of squares.
$n$ space-separated integers, $c_0,c_1,\ldots,c_{n-1}$, where each $c_i$ describes the number of coins at square $\boldsymbol{i}$.

Constraints

$1\leq T\leq10^4$
$1\leq n\leq100$
$0\leq c_i\leq10^9$

Output Format

For each test case, print the name of the winner on a new line (i.e., either $\textbf{First}$ or $\textbf{Second}$).

Sample Input
2
5
0 2 3 0 6
4
0 0 0 0

Sample Output
First
Second

Explanation

Explanation for $1^{st}$ testcase: 

The first player will shift one coin from $\textit{square}_2$ to $\textit{square}_0$. Hence, the second player is left with the squares $[1,2,2,0,6]$. Now whatever be his/her move is, the first player can always nullify the change by shifting a coin to the same square where he/she shifted it. Hence the last move is always played by the first player, so he wins. 

Exlanation for $2^{nd}$ testcase: 

There are no coins in any of the squares so the first player cannot make any move, hence second player wins.
"""

def nimble_game_winner(test_cases):
    results = []
    
    for case in test_cases:
        n, coins = case
        result = []
        
        for i in range(n):
            result.append(coins[i] % 2)
        
        xor = 0
        for i, num in enumerate(result):
            xor = xor ^ (i * num)
        
        if xor == 0:
            results.append('Second')
        else:
            results.append('First')
    
    return results