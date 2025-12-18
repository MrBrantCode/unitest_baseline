"""
QUESTION:
Implement a function `tower_of_hanoi_iterative(n)` that solves the Tower of Hanoi problem iteratively with a time complexity of O(n^2) and space complexity of O(n), where n is the number of disks. The function should return the minimum number of moves required to solve the problem.
"""

def tower_of_hanoi_iterative(n):
    # Create three stacks: "source", "auxiliary", and "destination".
    source = list(range(n, 0, -1))
    auxiliary = []
    destination = []

    # Initialize a variable "moves" to 0 to keep track of the number of moves.
    moves = 0

    # Initialize a variable "total_moves" to 2^n - 1, where n is the number of disks.
    total_moves = 2**n - 1

    # Repeat the following steps until "moves" becomes equal to "total_moves":
    while moves < total_moves:
        if len(source) > 0 and (len(destination) == 0 or source[-1] < destination[-1]):
            # Pop the top disk from the source stack and push it onto the destination stack.
            disk = source.pop()
            destination.append(disk)
        elif len(auxiliary) > 0 and (len(destination) == 0 or auxiliary[-1] < destination[-1]):
            # Pop the top disk from the auxiliary stack and push it onto the destination stack.
            disk = auxiliary.pop()
            destination.append(disk)
        elif len(source) > 0 and (len(auxiliary) == 0 or source[-1] < auxiliary[-1]):
            # Pop the top disk from the source stack and push it onto the auxiliary stack.
            disk = source.pop()
            auxiliary.append(disk)
        elif len(auxiliary) > 0 and (len(source) == 0 or auxiliary[-1] < source[-1]):
            # Pop the top disk from the auxiliary stack and push it onto the source stack.
            disk = auxiliary.pop()
            source.append(disk)

        # Increment "moves" by 1.
        moves += 1

    # Return the "moves" count, which represents the minimum number of moves required to solve the Tower of Hanoi problem iteratively.
    return moves