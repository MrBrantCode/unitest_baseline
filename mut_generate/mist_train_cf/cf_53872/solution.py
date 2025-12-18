"""
QUESTION:
Rami turns a dial on a machine 10 times, causing it to move 1 degree per turn. If this action is repeated simultaneously on multiple machines, calculate the total degrees moved. Write a function `total_degrees_turned` that takes the number of turns per machine and the number of machines as input and returns the total degrees moved.
"""

def total_degrees_turned(turns_per_machine, number_of_machines):
    return turns_per_machine * number_of_machines