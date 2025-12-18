"""
QUESTION:
Implement a function `TowerOfHanoi(n, from_rod, to_rod, aux_rod)` to solve the Tower of Hanoi problem. The function should take the number of discs `n` and the names of the rods as input, and print the sequence of moves required to move `n` discs from the `from_rod` to the `to_rod` using the `aux_rod`. The problem has the following restrictions: only one disc can be moved at a time, and a larger disc cannot be placed on top of a smaller disc.
"""

def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    if n == 1: 
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)