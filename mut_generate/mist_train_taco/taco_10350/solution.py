"""
QUESTION:
After you had helped George and Alex to move in the dorm, they went to help their friend Fedor play a new computer game «Call of Soldiers 3».

The game has (m + 1) players and n types of soldiers in total. Players «Call of Soldiers 3» are numbered form 1 to (m + 1). Types of soldiers are numbered from 0 to n - 1. Each player has an army. Army of the i-th player can be described by non-negative integer x_{i}. Consider binary representation of x_{i}: if the j-th bit of number x_{i} equal to one, then the army of the i-th player has soldiers of the j-th type. 

Fedor is the (m + 1)-th player of the game. He assume that two players can become friends if their armies differ in at most k types of soldiers (in other words, binary representations of the corresponding numbers differ in at most k bits). Help Fedor and count how many players can become his friends.


-----Input-----

The first line contains three integers n, m, k (1 ≤ k ≤ n ≤ 20; 1 ≤ m ≤ 1000).

The i-th of the next (m + 1) lines contains a single integer x_{i} (1 ≤ x_{i} ≤ 2^{n} - 1), that describes the i-th player's army. We remind you that Fedor is the (m + 1)-th player.


-----Output-----

Print a single integer — the number of Fedor's potential friends.


-----Examples-----
Input
7 3 1
8
5
111
17

Output
0

Input
3 3 3
1
2
3
4

Output
3
"""

def count_fedor_friends(n, m, k, armies):
    """
    Counts the number of players who can become Fedor's friends based on their army configurations.

    Parameters:
    - n (int): The number of types of soldiers.
    - m (int): The number of players (excluding Fedor).
    - k (int): The maximum number of differing soldier types for players to be considered friends.
    - armies (list of int): A list of integers representing the armies of the players, where the last element is Fedor's army.

    Returns:
    - int: The number of potential friends for Fedor.
    """
    fedor_army = armies[-1]
    friend_count = 0
    
    for i in range(m):
        player_army = armies[i]
        differing_bits = bin(player_army ^ fedor_army).count('1')
        if differing_bits <= k:
            friend_count += 1
    
    return friend_count