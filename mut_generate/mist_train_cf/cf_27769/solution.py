"""
QUESTION:
Write a function `calculate_average_sales` that takes a dictionary `areaDic` as input, where the keys are area names and the values are tuples containing the number of sales and the total amount of money for each area. The function should return a new dictionary with the area names as keys and the average amount of money spent per sale for each area as values. If an area has no sales, its average should not be calculated.
"""

def calculate_average_sales(areaDic):
    """
    Calculate the average amount of money spent per sale for each area.

    Args:
        areaDic (dict): A dictionary where the keys are area names and the values are tuples containing the number of sales and the total amount of money for each area.

    Returns:
        dict: A dictionary with the area names as keys and the average amount of money spent per sale for each area as values.
    """
    areaResult = dict()
    for area, (count, money) in areaDic.items():
        if count > 0:
            average = money / count
            areaResult[area] = average
    return areaResult