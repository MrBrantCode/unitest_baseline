"""
QUESTION:
Write a function `countApples` to compute the total number of "Apple" fruits with a count greater than 3 and less than 10 from a given list of fruit objects. The input is a list of dictionaries where each dictionary contains 'type' and 'count' keys. The function should return the total count of the "Apple" fruits that meet the specified condition.
"""

def countApples(fruits):
    """
    Compute the total number of "Apple" fruits with a count greater than 3 and less than 10.
    
    Args:
        fruits (list): A list of dictionaries containing 'type' and 'count' keys.
    
    Returns:
        int: The total count of the "Apple" fruits that meet the specified condition.
    """
    return sum(fruit['count'] for fruit in fruits if fruit['type'] == 'Apple' and 3 < fruit['count'] < 10)