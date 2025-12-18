"""
QUESTION:
Create a function called `calculate_total_revenue` that takes five parameters: the quantity of puzzles, dolls, bears, minions, and trucks sold, all of which are non-negative integers. Each type of toy has a fixed price: puzzles cost $2.6 each, dolls cost $3 each, bears cost $4.1 each, and minions and trucks do not have a fixed price given but their prices can be calculated as 8.1 and 2 per unit respectively from given example output for non-negative integers input. The function should calculate and return the total revenue generated from selling these toys.
"""

def calculate_total_revenue(puzzles, dolls, bears, minions, trucks):
    """
    Calculate the total revenue generated from selling toys.

    Parameters:
    puzzles (int): The quantity of puzzles sold.
    dolls (int): The quantity of dolls sold.
    bears (int): The quantity of bears sold.
    minions (int): The quantity of minions sold.
    trucks (int): The quantity of trucks sold.

    Returns:
    float: The total revenue generated from selling the toys.
    """
    return puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.1 + trucks * 2