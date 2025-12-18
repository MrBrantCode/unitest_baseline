"""
QUESTION:
Write a function `tower_of_hanoi(n, source, destination, auxiliary)` that uses recursion to solve the Tower of Hanoi problem for `n` discs initially stacked in increasing order of size on the `source` peg. The function should print the sequence of moves required to solve the problem and return the total number of moves, which is `2^n - 1`. The discs can be moved from the `source` peg to the `destination` peg using the `auxiliary` peg.
"""

def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        # Move n-1 discs from source to auxiliary peg
        tower_of_hanoi(n-1, source, auxiliary, destination)
        
        # Move the nth disc from source to destination peg
        print(f"Move disc {n} from {source} to {destination}")
        
        # Move the n-1 discs from auxiliary peg to destination peg
        tower_of_hanoi(n-1, auxiliary, destination, source)
    return 2**n - 1