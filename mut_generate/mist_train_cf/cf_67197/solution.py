"""
QUESTION:
Implement a recursive function `TowerOfHanoi(n, source, destination, auxiliary)` that solves the Tower of Hanoi problem for `n` disks, moving them from the `source` peg to the `destination` peg using the `auxiliary` peg, following the standard rules of the game. The function should print the sequence of moves required to solve the problem.
"""

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)