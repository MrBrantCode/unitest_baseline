"""
QUESTION:
Two pirates Polycarpus and Vasily play a very interesting game. They have n chests with coins, the chests are numbered with integers from 1 to n. Chest number i has a_{i} coins. 

Polycarpus and Vasily move in turns. Polycarpus moves first. During a move a player is allowed to choose a positive integer x (2·x + 1 ≤ n) and take a coin from each chest with numbers x, 2·x, 2·x + 1. It may turn out that some chest has no coins, in this case the player doesn't take a coin from this chest. The game finishes when all chests get emptied.

Polycarpus isn't a greedy scrooge. Polycarpys is a lazy slob. So he wonders in what minimum number of moves the game can finish. Help Polycarpus, determine the minimum number of moves in which the game can finish. Note that Polycarpus counts not only his moves, he also counts Vasily's moves.


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 100) — the number of chests with coins. The second line contains a sequence of space-separated integers: a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 1000), where a_{i} is the number of coins in the chest number i at the beginning of the game.


-----Output-----

Print a single integer — the minimum number of moves needed to finish the game. If no sequence of turns leads to finishing the game, print -1.


-----Examples-----
Input
1
1

Output
-1

Input
3
1 2 3

Output
3



-----Note-----

In the first test case there isn't a single move that can be made. That's why the players won't be able to empty the chests.

In the second sample there is only one possible move x = 1. This move should be repeated at least 3 times to empty the third chest.
"""

def minimum_moves_to_empty_chests(n, a):
    # Ensure the list 'a' has the correct length and format
    a = [0] + a
    
    # Check if the game can be finished based on the number of chests
    if n < 3 or n % 2 == 0:
        return -1
    
    ans = 0
    for x in range(n // 2, 0, -1):
        d = max(0, a[2 * x], a[2 * x + 1])
        ans += d
        a[x] -= d
    
    return ans + max(0, a[1])