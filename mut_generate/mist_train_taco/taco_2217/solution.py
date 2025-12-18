"""
QUESTION:
Alice and Bob are playing a game.

They start with a positive integer $n$ and take alternating turns doing operations on it. Each turn a player can subtract from $n$ one of its divisors that isn't $1$ or $n$. The player who cannot make a move on his/her turn loses. Alice always moves first.

Note that they subtract a divisor of the current number in each turn.

You are asked to find out who will win the game if both players play optimally.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases. Then $t$ test cases follow.

Each test case contains a single integer $n$ ($1 \leq n \leq 10^9$) — the initial number.


-----Output-----

For each test case output "Alice" if Alice will win the game or "Bob" if Bob will win, if both players play optimally.


-----Examples-----

Input
4
1
4
12
69
Output
Bob
Alice
Alice
Bob


-----Note-----

In the first test case, the game ends immediately because Alice cannot make a move.

In the second test case, Alice can subtract $2$ making $n = 2$, then Bob cannot make a move so Alice wins.

In the third test case, Alice can subtract $3$ so that $n = 9$. Bob's only move is to subtract $3$ and make $n = 6$. Now, Alice can subtract $3$ again and $n = 3$. Then Bob cannot make a move, so Alice wins.
"""

def determine_winner(n: int) -> str:
    """
    Determines the winner of the game between Alice and Bob given the initial number n.
    
    Parameters:
    n (int): The initial number from which the game starts.
    
    Returns:
    str: The winner of the game ("Alice" or "Bob").
    """
    if n == 1:
        return 'Bob'
    
    cnt = 0
    v = n
    while v % 2 == 0:
        v //= 2
        cnt += 1
    
    if v > 1:
        return 'Alice' if cnt > 0 else 'Bob'
    else:
        return 'Alice' if cnt % 2 == 0 else 'Bob'