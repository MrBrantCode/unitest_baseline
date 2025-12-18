"""
QUESTION:
There is a badminton championship in which $n$ players take part. The players are numbered from $1$ to $n$.

The championship proceeds as follows: player $1$ and player $2$ play a game, then the winner and player $3$ play a game, and then the winner and player $4$ play a game, and so on. So, $n-1$ games are played, and the winner of the last game becomes the champion. There are no draws in the games.

You want to find out the result of championship. Currently, you only know the following information:

Each player has either won $x$ games or $y$ games in the championship.

Given $n$, $x$, and $y$, find out if there is a result that matches this information.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^5$) — the number of test cases.

The only line of each test case contains three integers $n$, $x$, $y$ ($2 \le n \le 10^5$, $0 \le x, y < n$).

It is guaranteed that the sum of $n$ over all test cases doesn't exceed $2 \cdot 10^5$.


-----Output-----

Print the answer for each test case, one per line. If there is no result that matches the given information about $n$, $x$, $y$, print $-1$. Otherwise, print $n-1$ space separated integers, where the $i$-th integer is the player number of the winner of the $i$-th game.

If there are multiple valid results, print any.


-----Examples-----

Input
5
5 2 0
8 1 2
3 0 0
2 0 1
6 3 0
Output
1 1 4 4
-1
-1
2 
-1


-----Note-----

In the first test case, player $1$ and player $4$ won $x$ times, player $2$ and player $3$ won $y$ times.

In the second, third, and fifth test cases, no valid result exists.
"""

def find_championship_result(n, x, y):
    """
    Determines the result of the badminton championship based on the given parameters.

    Parameters:
    n (int): The number of players.
    x (int): The number of games won by some players.
    y (int): The number of games won by other players.

    Returns:
    list: A list of integers representing the winners of each game, or -1 if no valid result exists.
    """
    if x == 0 and y == 0:
        return -1
    elif x == 0 or y == 0:
        number = x if x != 0 else y
        if (n - 1) % number != 0:
            return -1
        else:
            player = list(range(1, n + 1))
            player = player[1::number]
            winner = [1] + player[1:]
            for_print = []
            for each in winner:
                for_print += [each] * number
            return for_print
    else:
        return -1