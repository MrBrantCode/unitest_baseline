"""
QUESTION:
Amr bought a new video game "Guess Your Way Out!". The goal of the game is to find an exit from the maze that looks like a perfect binary tree of height h. The player is initially standing at the root of the tree and the exit from the tree is located at some leaf node. 

Let's index all the leaf nodes from the left to the right from 1 to 2^{h}. The exit is located at some node n where 1 ≤ n ≤ 2^{h}, the player doesn't know where the exit is so he has to guess his way out!

Amr follows simple algorithm to choose the path. Let's consider infinite command string "LRLRLRLRL..." (consisting of alternating characters 'L' and 'R'). Amr sequentially executes the characters of the string using following rules:  Character 'L' means "go to the left child of the current node";  Character 'R' means "go to the right child of the current node";  If the destination node is already visited, Amr skips current command, otherwise he moves to the destination node;  If Amr skipped two consecutive commands, he goes back to the parent of the current node before executing next command;  If he reached a leaf node that is not the exit, he returns to the parent of the current node;  If he reaches an exit, the game is finished. 

Now Amr wonders, if he follows this algorithm, how many nodes he is going to visit before reaching the exit?


-----Input-----

Input consists of two integers h, n (1 ≤ h ≤ 50, 1 ≤ n ≤ 2^{h}).


-----Output-----

Output a single integer representing the number of nodes (excluding the exit node) Amr is going to visit before reaching the exit by following this algorithm.


-----Examples-----
Input
1 2

Output
2
Input
2 3

Output
5
Input
3 6

Output
10
Input
10 1024

Output
2046


-----Note-----

A perfect binary tree of height h is a binary tree consisting of h + 1 levels. Level 0 consists of a single node called root, level h consists of 2^{h} nodes called leaves. Each node that is not a leaf has exactly two children, left and right one. 

Following picture illustrates the sample test number 3. Nodes are labeled according to the order of visit.

[Image]
"""

def count_nodes_before_exit(h: int, n: int) -> int:
    """
    Calculates the number of nodes visited before reaching the exit in a perfect binary tree of height h,
    where the exit is located at the nth leaf node from the left.

    Parameters:
    h (int): The height of the binary tree (1 ≤ h ≤ 50).
    n (int): The position of the exit node among the leaf nodes (1 ≤ n ≤ 2^h).

    Returns:
    int: The number of nodes visited before reaching the exit.
    """
    height_nodes = [1 for _ in range(51)]
    for height in range(1, 51):
        height_nodes[height] = 2 ** height + height_nodes[height - 1]
    
    cur_pos = 2 ** (h - 1)
    depth = h
    add = 2 ** (h - 1)
    direction = -1
    total = 0
    
    while True:
        if depth == 0:
            break
        if (cur_pos >= n and direction == -1) or (cur_pos < n and direction == 1):
            total += 1
            depth -= 1
            add //= 2
            cur_pos += direction * add
        else:
            total += height_nodes[depth - 1]
        direction *= -1
    
    return total