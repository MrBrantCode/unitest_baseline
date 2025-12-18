"""
QUESTION:
Petya and Vasya are playing a game. Petya's got n non-transparent glasses, standing in a row. The glasses' positions are indexed with integers from 1 to n from left to right. Note that the positions are indexed but the glasses are not.

First Petya puts a marble under the glass in position s. Then he performs some (possibly zero) shuffling operations. One shuffling operation means moving the glass from the first position to position p_1, the glass from the second position to position p_2 and so on. That is, a glass goes from position i to position p_{i}. Consider all glasses are moving simultaneously during one shuffling operation. When the glasses are shuffled, the marble doesn't travel from one glass to another: it moves together with the glass it was initially been put in.

After all shuffling operations Petya shows Vasya that the ball has moved to position t. Vasya's task is to say what minimum number of shuffling operations Petya has performed or determine that Petya has made a mistake and the marble could not have got from position s to position t.


-----Input-----

The first line contains three integers: n, s, t (1 ≤ n ≤ 10^5; 1 ≤ s, t ≤ n) — the number of glasses, the ball's initial and final position. The second line contains n space-separated integers: p_1, p_2, ..., p_{n} (1 ≤ p_{i} ≤ n) — the shuffling operation parameters. It is guaranteed that all p_{i}'s are distinct.

Note that s can equal t.


-----Output-----

If the marble can move from position s to position t, then print on a single line a non-negative integer — the minimum number of shuffling operations, needed to get the marble to position t. If it is impossible, print number -1.


-----Examples-----
Input
4 2 1
2 3 4 1

Output
3

Input
4 3 3
4 1 3 2

Output
0

Input
4 3 4
1 2 3 4

Output
-1

Input
3 1 3
2 1 3

Output
-1
"""

def minimum_shuffles(n, s, t, p):
    """
    Calculate the minimum number of shuffling operations needed to move the marble from position s to position t.

    Parameters:
    n (int): The number of glasses.
    s (int): The initial position of the marble.
    t (int): The final position of the marble.
    p (list of int): The shuffling operation parameters.

    Returns:
    int: The minimum number of shuffling operations needed, or -1 if it is impossible.
    """
    if s == t:
        return 0
    
    step = 0
    current_position = s
    
    while step < n:
        next_position = p[current_position - 1]
        step += 1
        
        if next_position == t:
            return step
        
        current_position = next_position
    
    return -1