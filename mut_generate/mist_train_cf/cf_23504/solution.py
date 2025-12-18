"""
QUESTION:
Write a recursive function `TowerOfHanoi` that takes four parameters: the number of disks `n`, and the names of three rods `from_rod`, `to_rod`, and `aux_rod`. The function should print the sequence of moves required to move `n` disks from `from_rod` to `to_rod`, using `aux_rod` as a temporary storage. The function should not take any additional input or return any value, only print the moves.
"""

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    """
    Prints the sequence of moves required to move n disks from from_rod to to_rod, 
    using aux_rod as a temporary storage.

    Args:
    n (int): The number of disks.
    from_rod (str): The name of the rod where disks are initially located.
    to_rod (str): The name of the rod where disks need to be moved.
    aux_rod (str): The name of the auxiliary rod used for temporary storage.
    """
    if n == 1: 
        print("Move disk 1 from rod", from_rod, "to rod", to_rod) 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)