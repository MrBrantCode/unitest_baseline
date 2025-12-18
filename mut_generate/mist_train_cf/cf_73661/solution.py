"""
QUESTION:
Create a function called mann_whitney_u that calculates the U statistic in the Mann-Whitney U test. The function should take two integers, n1 and n2, and an integer R1 as input, and return the U statistic U1. The formula for U1 is U1 = n1(n1+1)/2 + n1*n2 - R1.
"""

def mann_whitney_u(n1, n2, R1):
    """
    Calculate the U statistic in the Mann-Whitney U test.

    Parameters:
    n1 (int): The size of the first group.
    n2 (int): The size of the second group.
    R1 (int): The rank sum of the first group.

    Returns:
    int: The U statistic U1.
    """
    U1 = n1*(n1+1)//2 + n1*n2 - R1
    return U1