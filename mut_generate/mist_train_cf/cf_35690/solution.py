"""
QUESTION:
Implement a function `towers_of_hanoi` that takes an integer `n` representing the number of disks as input and returns a list of tuples representing the sequence of moves required to solve the Towers of Hanoi problem. Each tuple should contain two integers representing the source rod and the destination rod for a single move, with rods labeled 1, 2, and 3. The function should follow the standard Towers of Hanoi rules: only one disk can be moved at a time, each move consists of taking the top disk from one of the stacks and placing it on top of another stack, and no disk may be placed on top of a smaller disk.
"""

def towers_of_hanoi(n):
    """
    Solve the Towers of Hanoi problem for n disks.

    Args:
    n: An integer representing the number of disks.

    Returns:
    A list of tuples representing the sequence of moves required to solve the problem.
    Each tuple contains two integers representing the source rod and the destination rod for a single move.
    """
    moves = []

    def hanoi(n, source, target, auxiliary):
        if n == 1:
            moves.append((source, target))
        else:
            hanoi(n - 1, source, auxiliary, target)
            moves.append((source, target))
            hanoi(n - 1, auxiliary, target, source)

    hanoi(n, 1, 3, 2)
    return moves