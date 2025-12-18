"""
QUESTION:
Write a function called `calculate_data_skew` to calculate the data skew in a Hadoop ecosystem. This function should take a dictionary where the keys are the node names and the values are the corresponding data amounts as input, and return the data skew as a float value. The data skew is defined as the ratio of the maximum data amount to the average data amount. 

The function should also handle cases where the input dictionary is empty, in which case it should return 0.0.
"""

def calculate_data_skew(data_amounts):
    """
    Calculate the data skew in a Hadoop ecosystem.

    The data skew is defined as the ratio of the maximum data amount to the average data amount.

    Args:
        data_amounts (dict): A dictionary where the keys are the node names and the values are the corresponding data amounts.

    Returns:
        float: The data skew as a float value. Returns 0.0 if the input dictionary is empty.
    """
    if not data_amounts:
        return 0.0

    max_data_amount = max(data_amounts.values())
    average_data_amount = sum(data_amounts.values()) / len(data_amounts)

    return max_data_amount / average_data_amount