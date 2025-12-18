"""
QUESTION:
Write a function `TowerOfHanoi(n, source, destination, auxiliary)` to solve the Tower of Hanoi problem, which moves `n` disks from the `source` rod to the `destination` rod using the `auxiliary` rod. The function should print the sequence of moves to solve the problem. The solution should use recursion and handle any number of disks.
"""

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)