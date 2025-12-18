"""
QUESTION:
Design a function called `towersOfHanoi` that takes four parameters: the number of disks `n` and three characters representing the names of the rods `from_rod`, `to_rod`, and `aux_rod`. The function should print the sequence of moves required to solve the Towers of Hanoi problem. The function should not return any value and should use recursion to solve the problem.
"""

def towers_of_hanoi(n, from_rod, to_rod, aux_rod):
    """
    Prints the sequence of moves required to solve the Towers of Hanoi problem.

    Args:
        n (int): The number of disks.
        from_rod (str): The name of the rod where disks are initially located.
        to_rod (str): The name of the rod where disks need to be moved.
        aux_rod (str): The name of the auxiliary rod.
    """

    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    
    towers_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    towers_of_hanoi(n - 1, aux_rod, to_rod, from_rod)