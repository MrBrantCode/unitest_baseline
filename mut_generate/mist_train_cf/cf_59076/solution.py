"""
QUESTION:
Write a function called calculate_total_cost that takes two parameters: num_puzzles and cost_per_puzzle. The function should calculate and return the overall total cost of the puzzles sold inclusive of tax. The function should not take any other parameters. The function should return the result as an integer.
"""

def calculate_total_cost(num_puzzles, cost_per_puzzle):
    """
    Calculate the total cost of puzzles sold inclusive of tax.

    Args:
        num_puzzles (int): The number of puzzles sold.
        cost_per_puzzle (int): The cost of each puzzle.

    Returns:
        int: The total cost of puzzles sold.
    """
    # Calculate the overall total cost by multiplying the number of puzzles by the cost of each puzzle
    total_cost = num_puzzles * cost_per_puzzle
    return total_cost