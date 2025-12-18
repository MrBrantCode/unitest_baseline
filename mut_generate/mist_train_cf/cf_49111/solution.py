"""
QUESTION:
Write a function called `calculate_marbles_joe` that takes an integer representing the number of marbles Dani owns as input and returns the exact count of marbles Joe has. It is given that Dani has exactly 5 times the number of marbles owned by Joe.
"""

def calculate_marbles_joe(marbles_dani):
    """
    This function calculates the number of marbles Joe owns given the number of marbles Dani has.
    
    Parameters:
    marbles_dani (int): The number of marbles Dani owns.
    
    Returns:
    int: The number of marbles Joe owns.
    """
    marbles_joe = marbles_dani / 5
    return marbles_joe