"""
QUESTION:
Implement the `TowerOfHanoi` function in Python that solves the Tower of Hanoi problem for a given number of disks `n`. The function should take four parameters: `n` (the number of disks), `from_` (the starting tower), `to` (the destination tower), and `aux` (the auxiliary tower). The function should print the steps to move the disks from one tower to another and should be able to handle up to 20 disks within a time limit of 1 second.
"""

def TowerOfHanoi(n, from_, to, aux):
    # base case
    if n == 1:
        print(f"Move disk 1 from {from_} to {to}")
        return

    # Step 1: Move n-1 disks from 'from_' to auxiliary tower, Use 'to' as auxiliary tower
    TowerOfHanoi(n-1, from_, aux, to)

    # Step 2: Move the nth disk from 'from_' to 'to'
    print(f"Move disk {n} from {from_} to {to}")

    # Step 3: Move the n-1 disks that we left on auxiliary tower to 'to'
    # Use 'from_' as auxiliary tower
    TowerOfHanoi(n-1, aux, to, from_)