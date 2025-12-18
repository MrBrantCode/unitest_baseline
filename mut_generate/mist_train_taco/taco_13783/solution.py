"""
QUESTION:
Nim is a famous game in which two players take turns removing items from $n$ distinct piles. During each turn, a player must remove one or more items from a single, non-empty pile. The winner of the game is whichever player removes the last item from the last non-empty pile.

John and Kate modified Nim by adding the following rule, which they call a Zero-Move:

For each non-empty pile, either player can remove $0$ items from that pile and have it count as their move; however, this move can only be performed once per pile by either player. For example, let's say pile $\boldsymbol{i}$ initially has $p_i=2$ items in it. If John decides to use a Zero-Move on pile $\boldsymbol{i}$, then neither John nor Kate can perform another Zero-Move on pile $\boldsymbol{i}$; that said, either player is free to perform a Zero-Move on any other non-empty pile that hasn't had a Zero-Move performed on it yet.

John and Kate play $\mathrm{~g~}$ games of Zero-Move Nim. Given the number of items in each pile for each game, determine whether or not John can win the game if he always moves first and each player always moves optimally (i.e., never makes a move that causes them to lose if some better, winning move exists). For each game, print W on a new line if John can win; otherwise, print L instead.

Input Format

The first line contains an integer, $\mathrm{~g~}$, denoting the number of games. The $2\cdot g$ subsequent lines describe each game over two lines:

The first line contains an integer, $n$, denoting the number of heaps.
The second line contains $n$ space-separated integers describing $p_0,p_1,\ldots,p_{n-1}$. 

Constraints

$1\leq g\leq10$  
$1\leq n\leq10$  
$1\leq p_i<2^{30}$  

Subtasks   

For $\textbf{40%}$ of the test cases, $1\leq p_i<2^7$  
For $\textbf{60%}$ of the test cases, $1\leq p_i<2^{17}$

Output Format

For each game, print W on a new line if John will win; otherwise, print L instead.

Sample Input 0
2
2
1 2
2
2 2

Sample Output 0
W
L

Explanation 0

John and Kate play the following $g=2$ games:

We have two piles, $p_0=1$ and $p_1=2$. John removes $1$ item from $p_1$, so $p_1=2-1=1$. Now that there is only $1$ item in each pile, gameplay can proceed in either of the following ways:

Kate removes the last object from one pile, then John removes the last object from the other pile.
Kate uses a Zero-Move on one of the piles, and John uses a Zero-Move on the other pile. Next, Kate must take the last object from one pile, at which point John removes the last object from the other pile.          

Because John always wins in either scenario, we print W on a new line.

John cannot win this game because the two piles are of equal size and Kate has an opportunity to counter any move he makes by performing the same action. Consider the following scenarios:

If John uses a Zero-Move on one pile, Kate can use a Zero-Move on the other pile (meaning the piles still have the same configuration after both players move).
If John removes one element from a pile, Kate can remove one element from the other pile so that both remaining piles contain one element when John takes his next turn. He would then be forced to empty one of the piles, leaving Kate to make the winning move by emptying the last pile.
If John removes both elements from one of the piles, Kate can remove both elements from the other pile and win the game.      

Because John always loses this game, we print L on a new line.
"""

def determine_nim_winner(g, games):
    """
    Determines the winner of multiple games of Zero-Move Nim.

    Parameters:
    g (int): The number of games.
    games (list of lists): A list where each sublist contains integers representing the number of items in each pile for a game.

    Returns:
    list of str: A list of 'W' or 'L' strings indicating whether John can win each game ('W' for win, 'L' for lose).
    """
    results = []
    for game in games:
        result = reduce(xor, [x + 1 if x & 1 else x - 1 for x in game], 0)
        results.append('W' if result else 'L')
    return results