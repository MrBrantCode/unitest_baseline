"""
QUESTION:
Create a function named `TowerOfHanoi` that takes four parameters: `n` (the number of disks), `source` (the starting rod), `destination` (the target rod), and `auxiliary` (the extra rod). Write a recursive algorithm that prints the sequence of moves required to solve the Tower of Hanoi problem. The function should move `n` disks from the `source` rod to the `destination` rod, using the `auxiliary` rod as a temporary storage.
"""

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print ("Move disk 1 from rod", source, "to rod", destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk", n, "from rod", source, "to rod", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)