"""
QUESTION:
Welcome to PC Koshien, players. At PC Koshien, competitions are currently being held in a total of three categories: programming category, mobile category, and Ichimai's picture CG category.

Given the number of participants in each department, create a program that calculates the total number of participants.



Input

The input is given in the following format.


p m c


The input is one line, the number of participants in the programming department p (0 ≤ p ≤ 10000), the number of participants in the mobile department m (0 ≤ m ≤ 10000), the number of participants in the Ichimai picture CG department c (0) ≤ c ≤ 10000) is given.

Output

Output the total number of participants on one line.

Examples

Input

10 10 20


Output

40


Input

100 0 0


Output

100


Input

1000 1000 1000


Output

3000
"""

def calculate_total_participants(p: int, m: int, c: int) -> int:
    """
    Calculate the total number of participants across three departments.

    Parameters:
    p (int): Number of participants in the programming department.
    m (int): Number of participants in the mobile department.
    c (int): Number of participants in the Ichimai picture CG department.

    Returns:
    int: The total number of participants.
    """
    return p + m + c