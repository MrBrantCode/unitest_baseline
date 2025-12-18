"""
QUESTION:
Write a function named `move_disks(n, source, auxiliary, destination)` that prints the steps required to solve the modified Towers of Hanoi problem, where `n` is the number of disks, `source` is the starting tower, `auxiliary` is the auxiliary tower, and `destination` is the destination tower. Each disk can only be moved to a tower that is at least two positions away from its current tower. Assume that the towers are labeled 'A', 'B', 'C', etc., and that the distance between two towers is determined by the absolute difference in their ASCII values.
"""

def move_disks(n, source, auxiliary, destination):
    if n == 0:
        return

    move_disks(n-1, source, destination, auxiliary)

    if is_possible_to_move(source, destination):
        move_disk(source, destination)
    else:
        move_disk(source, auxiliary)

    move_disks(n-1, auxiliary, source, destination)

def is_possible_to_move(source, destination):
    return abs(ord(source) - ord(destination)) >= 2

def move_disk(source, destination):
    print(f"Move disk from {source} to {destination}")