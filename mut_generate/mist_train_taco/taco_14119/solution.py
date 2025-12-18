"""
QUESTION:
Alice and Brown are brothers in a family and each receives pocket money in celebration of the coming year. They are very close and share the total amount of the money fifty-fifty. The pocket money each receives is a multiple of 1,000 yen.

Write a program to calculate each one’s share given the amount of money Alice and Brown received.



Input

The input is given in the following format.


a b


A line of data is given that contains two values of money: a (1000 ≤ a ≤ 50000) for Alice and b (1000 ≤ b ≤ 50000) for Brown.

Output

Output the amount of money each of Alice and Brown receive in a line.

Examples

Input

1000 3000


Output

2000


Input

5000 5000


Output

5000


Input

1000 2000


Output

1500
"""

def calculate_shared_pocket_money(a: int, b: int) -> int:
    """
    Calculate the amount of money each of Alice and Brown receive when they share their total pocket money equally.

    Parameters:
    a (int): The amount of money Alice received.
    b (int): The amount of money Brown received.

    Returns:
    int: The amount of money each of Alice and Brown receive.
    """
    return (a + b) // 2