"""
QUESTION:
Design a function `harmonic_mean` that calculates the harmonic mean from a given dictionary where keys represent the values and values represent the frequency of each value. The function should return the harmonic mean. Assume all input values are positive.
"""

def harmonic_mean(dict_values):
    """
    Calculate the harmonic mean from a dictionary of values and their frequencies.

    Parameters:
    dict_values (dict): A dictionary where keys are values and values are frequencies.

    Returns:
    float: The harmonic mean.
    """
    total_num = sum(dict_values.values())
    harmonic_sum = sum([freq / value for value, freq in dict_values.items()])
    return total_num / harmonic_sum