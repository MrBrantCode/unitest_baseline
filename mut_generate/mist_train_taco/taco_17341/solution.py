"""
QUESTION:
A group of people played a game. All players had distinct scores, which are positive integers.

Takahashi knows N facts on the players' scores. The i-th fact is as follows: the A_i-th highest score among the players is B_i.

Find the maximum possible number of players in the game.

Constraints

* 1 \leq N \leq 10^5
* 1 \leq A_i \leq 10^9(1\leq i\leq N)
* 0 \leq B_i \leq 10^9(1\leq i\leq N)
* If i ≠ j, A_i ≠ A_j.
* There exists a possible outcome of the game that are consistent with the facts.
* All input values are integers.

Inputs

Input is given from Standard Input in the following format:


N
A_1 B_1
:
A_N B_N


Outputs

Print the maximum possible number of players in the game.

Examples

Input

3
4 7
2 9
6 2


Output

8


Input

5
1 10
3 6
5 2
4 4
2 8


Output

7


Input

2
1 1000000000
1000000000 1


Output

1000000001
"""

def max_possible_players(N, AB):
    """
    Calculate the maximum possible number of players in the game based on the given facts.

    Parameters:
    N (int): The number of facts.
    AB (list of tuples): A list of tuples where each tuple contains two integers (A_i, B_i).

    Returns:
    int: The maximum possible number of players in the game.
    """
    v = max(AB, key=lambda x: x[0])
    return v[0] + v[1]