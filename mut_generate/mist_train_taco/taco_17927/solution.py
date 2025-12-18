"""
QUESTION:
Kitty and Katty have $N$ plastic blocks. They label the blocks with sequential numbers from $\mbox{1}$ to $N$ and begin playing a game in turns, with Kitty always taking the first turn. The game's rules are as follows:

For each turn, the player removes $2$ blocks, $\mbox{A}$ and $\mbox{B}$, from the set. They calculate $A-B$, write the result on a new block, and insert the new block into the set. 
The game ends when only $\mbox{1}$ block is left. The winner is determined by the value written on the final block, $\mbox{X}$:
If $X\%3=1$, then Kitty wins.
If $X\%3=2$, then Katty wins.
If $X\%3=0$, then the player who moved last wins.

Recall that $\%$ is the Modulo Operation.

Given the value of $N$, can you find and print the name of the winner? Assume that both play optimally.

Note: The selection order for $\mbox{A}$ and $\mbox{B}$ matters, as sometimes $A-B\neq B-A$. The diagram below shows an initial set of blocks where $N=5$. If $A=2$ and $B=3$, then the newly inserted block is labeled $-1$; alternatively, if $A=3$ and $B=2$, the newly inserted block is labeled $\mbox{1}$.

Input Format

The first line contains a single positive integer, $\mathbf{T}$ (the number of test cases or games). 

The $\mathbf{T}$ subsequent lines each contain an integer, $N$ (the number of blocks for that test case).

Constraints 

$1\leq T\leq100$

$1\leq N\leq10^5$

Output Format

For each test case, print the name of the winner (i.e.: either Kitty or Katty) on a new line.

Sample Input
2
2
3

Sample Output
Kitty
Katty

Explanation

Test Case 0: 

$N=2$ so there are two blocks labeled $\mbox{1}$ and $2$. Kitty chooses $A=2$ and $B=1$, then inserts a new block with  the label $\mbox{1}$ (the result of $2-1$). The game ends, as there is now only $\mbox{I}$ block in the set. The label on the last block, $\mbox{X}$, is $\mbox{1}$, so we calculate $result=1\%3=1$. Because  $result=1$, Kitty wins and we print Kitty on a new line.

Test Case 1: 

$N=3$, so there are three blocks labeled $\mbox{1}$, $2$, and $3$. No matter how Kitty makes the first move, Katty will win. If Kitty chooses $A=3$ and $B=2$ on the first move and inserts a block labeled $\mbox{I}$ (the result of $3-2$), the set of blocks becomes $\{1,1\}$. Katty then must choose $A=1$ and $B=1$ and insert a new block labeled $\mbox{o}$ (the result of $1-1$). The game ends, as there is now only $\mbox{I}$ block in the set. The label on the last block, $\mbox{X}$, is $\mbox{0}$, so we calculate $result=0\%3=0$. Because $result=0$ and Katty made the last move, Katty wins and we print Katty on a new line.
"""

def determine_winner(n: int) -> str:
    """
    Determines the winner of the game between Kitty and Katty based on the number of plastic blocks.

    Parameters:
    n (int): The number of plastic blocks.

    Returns:
    str: The name of the winner ("Kitty" or "Katty").
    """
    if n == 1:
        return 'Kitty'
    elif n % 2 == 1:
        return 'Katty'
    else:
        return 'Kitty'