"""
QUESTION:
Create a function `hanoi(num_disks, from_peg, to_peg, aux_peg)` that prints the steps to solve the Tower of Hanoi problem, where `num_disks` is the number of disks, and `from_peg`, `to_peg`, and `aux_peg` represent the source, destination, and auxiliary pegs respectively. The function should recursively print the steps to move the disks from the source peg to the destination peg, using the auxiliary peg as needed.
"""

def hanoi(num_disks, from_peg, to_peg, aux_peg):
    if num_disks == 1:
        print("Move disk 1 from peg", from_peg,"to peg", to_peg)
        return

    hanoi(num_disks-1, from_peg, aux_peg, to_peg)
    print("Move disk",num_disks,"from peg",from_peg,"to peg",to_peg)
    hanoi(num_disks-1, aux_peg, to_peg, from_peg)