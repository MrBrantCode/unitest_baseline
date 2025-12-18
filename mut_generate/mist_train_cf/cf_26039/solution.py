"""
QUESTION:
Write a function `tower_of_hanoi(n, source, aux, dest)` to solve the Tower of Hanoi puzzle. The function should take four parameters: `n`, the number of disks, and three rods `source`, `aux`, and `dest`, where `source` is the starting rod, `aux` is the auxiliary rod, and `dest` is the destination rod. The function should print the sequence of moves required to solve the puzzle, with each move specified as "Move disk x from rod y to rod z".
"""

def tower_of_hanoi(n, source, aux, dest): 
    if n == 1: 
        print("Move disk 1 from rod", source, "to rod", dest)
        return
    tower_of_hanoi(n-1, source, dest, aux) 
    print("Move disk", n, "from rod", source, "to rod", dest) 
    tower_of_hanoi(n-1, aux, source, dest)