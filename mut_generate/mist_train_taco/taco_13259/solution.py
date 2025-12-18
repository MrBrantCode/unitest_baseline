"""
QUESTION:
As usual Gary and Flo are sitting at their favourite burger restaurant called Jim's Burgers. They want to treat themselves with delicious burger after an interesting day with lots of competitive programming. So they have ordered their burgers and are waiting for them. But with nothing to do, they get bored and decide to play a game.

The game is played on a sheet of paper with $n$ rows and $m$ columns and goes as follows: 

Flo places his white lotus tile somewhere at the top row and Gary places a caterpillar tile somewhere on the bottom row. Flo begins the game and their turns alternate. Flo can move his tile to any of the 8 adjacent cells, while Gary's caterpillar tile can only move  left or right, or stay at the same cell. Of course, they cannot step outside of the grid. Flo's goal is to catch Gary as fast as possible, that is, with the minimum number of moves, while Gary (with the caterpillar tile) has to survive for as long as possible.  

Now they are wondering: If they place their tiles in the corresponding rows and some random columns, what is the expected number of moves Flo has to make to win the game (assuming they will play optimally)? 

Can you help them answer this question?

Constraints

$2\leq n,m\leq5000$

Input Format

You will be given two space separated integers $n$ and $m$, denoting the number of rows and the number of columns on the board respectively. 

Output Format

Output the answer in one line. 

Note: The answer will be considered valid if it differs from the correct answer by at most $\mathbf{10^{-6}}$.

Sample input

2 3

Sample output

1.2222222

Consider the pair $(x,y)$ as the starting column of the lotus and the starting column of the caterpillar respectively. 

For $n=2$ and $m=3$ we get the following scenario. 

$(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3)$ will lead to 1 move. 
The remaining pairs $(1,3)$ and $(3,1)$ will lead to 2 moves. So the expected value  is $\frac{1+1+1+1+1+1+1+2+2}{9}=1.222..$
"""

def calculate_expected_moves(n: int, m: int) -> float:
    """
    Calculate the expected number of moves Flo has to make to catch Gary on a grid of size n x m.

    Parameters:
    n (int): The number of rows on the board.
    m (int): The number of columns on the board.

    Returns:
    float: The expected number of moves Flo has to make to win the game.
    """
    if m <= n:
        return n - 1
    if n < m:
        out = 2 * m * (m ** 2 - 3 * m + 2) + (n - 3) * (n - 2) * (n - 1)
        out /= 3
        out += m * (n - 1) + 2 * (m - 1) * (n - 1)
    return out / m ** 2