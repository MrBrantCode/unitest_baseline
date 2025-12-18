"""
QUESTION:
Write a function `TowerOfHanoi` that takes four parameters: the number of disks `n`, and the names of three rods `source`, `destination`, and `auxiliary`. The function should print the sequence of moves to solve the Tower of Hanoi problem, where `n` disks are initially on the `source` rod and need to be moved to the `destination` rod using the `auxiliary` rod.
"""

def TowerOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from rod",source,"to rod",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from rod",source,"to rod",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)