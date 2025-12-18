"""
QUESTION:
Write a function `solveTowerOfHanoi` that takes four parameters: the number of disks (`n`), and the names of the source, auxiliary, and destination rods. The function should print out the sequence of moves required to solve the Tower of Hanoi problem. The problem starts with `n` disks on the source rod, and the goal is to move them to the destination rod, subject to the constraint that a larger disk can never be placed on top of a smaller one.
"""

def solveTowerOfHanoi(n, source, auxiliary, destination): 
  if n==1: 
    print("Move disk 1 from source",source,"to destination",destination) 
    return 
  solveTowerOfHanoi(n-1, source, destination, auxiliary) 
  print("Move disk",n,"from source",source,"to destination",destination) 
  solveTowerOfHanoi(n-1, auxiliary, source, destination)