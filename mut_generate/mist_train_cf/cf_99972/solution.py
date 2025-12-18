"""
QUESTION:
Write a function named `top_three_vegetables` that takes in a list of tuples, where each tuple contains the name of a vegetable and its popularity ranking. The function should return a list of the names of the top three most popular vegetables. The input list can contain any number of tuples, and the popularity rankings are not necessarily consecutive or unique.
"""

def top_three_vegetables(vegetables):
    """
    Returns a list of the names of the top three most popular vegetables.

    Args:
        vegetables (list): A list of tuples, where each tuple contains the name of a vegetable and its popularity ranking.

    Returns:
        list: A list of the names of the top three most popular vegetables.
    """
    sorted_vegetables = sorted(vegetables, key=lambda veg: veg[1], reverse=True)
    return [veg[0] for veg in sorted_vegetables[:3]]