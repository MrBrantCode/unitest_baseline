"""
QUESTION:
Consider the following game:

There are two players, First and Second, sitting in front of a pile of $n$ stones. First always plays first.
There is a set, $\mbox{S}$, of $m$ distinct integers defined as $S=\{s_0,s_1,\ldots,s_{m-1}\}$.
The players move in alternating turns. During each turn, a player chooses some $s_i\in S$ and splits one of the piles into exactly $s_i$ smaller piles of equal size. If no $s_i$ exists that will split one of the available piles into exactly $s_i$ equal smaller piles, the player loses.
Both players always play optimally.

Given $n$, $m$, and the contents of $\mbox{S}$, find and print the winner of the game. If First wins, print First; otherwise, print Second.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the size of the initial pile) and $m$ (the size of the set). 

The second line contains $m$ distinct space-separated integers describing the respective values of $s_0,s_1,\ldots,s_{m-1}$.

Constraints

$1\leq n\leq10^{18}$
$1\leq m\leq10$
$2\leq s_i\leq10^{18}$

Output Format

Print First if the First player wins the game; otherwise, print Second.

Sample Input 0
15 3
5 2 3

Sample Output 0
Second

Explanation 0

The initial pile has $n=15$ stones, and $S=\{5,2,3\}$. During First's initial turn, they have two options:

Split the initial pile into $5$ equal piles, which forces them to lose after the following sequence of turns: 

Split the initial pile into $3$ equal piles, which forces them to lose after the following sequence of turns: 

Because First never has any possible move that puts them on the path to winning, we print Second as our answer.
"""

def determine_winner(n: int, S: list) -> str:
    """
    Determines the winner of the game given the initial number of stones `n` and the set `S` of possible splits.

    Parameters:
    n (int): The initial number of stones.
    S (list): A list of integers representing the possible splits.

    Returns:
    str: The winner of the game, either "First" or "Second".
    """
    hist = {}

    def foo(n, a):
        if n in hist:
            return hist[n]
        for x in a:
            if n % x == 0:
                if x % 2 == 0:
                    hist[n] = True
                    return True
                nn = n // x
                if not foo(nn, a):
                    hist[n] = True
                    return True
        hist[n] = False
        return False

    if foo(n, S):
        return 'First'
    else:
        return 'Second'