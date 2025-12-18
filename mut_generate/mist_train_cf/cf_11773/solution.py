"""
QUESTION:
Develop a function called `move_disks` that solves the modified Towers of Hanoi problem with the additional constraint that each disk can only be moved to a tower that is at least two positions away from its current tower. The function should take four parameters: the number of disks to be moved (n), the source tower, the auxiliary tower, and the destination tower. The function should print the necessary steps to solve the problem.
"""

def move_disks(n, source, auxiliary, destination):
    def is_possible_to_move(source, destination):
        # Check if the distance between the source and destination is at least 2
        return abs(ord(source) - ord(destination)) >= 2

    def move_disk(source, destination):
        print(f"Move disk from {source} to {destination}")

    if n == 0:
        return

    move_disks(n-1, source, destination, auxiliary)

    if is_possible_to_move(source, destination):
        move_disk(source, destination)
    else:
        move_disk(source, auxiliary)

    move_disks(n-1, auxiliary, source, destination)