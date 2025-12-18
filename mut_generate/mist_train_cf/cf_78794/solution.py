"""
QUESTION:
Write a function called `calculate_average` that takes a dictionary `d` as input, where each key corresponds to either a single integer or a list of integers. The function should calculate and return the average of all the integers in the dictionary, considering each integer in the lists.
"""

def calculate_average(d):
    """
    Calculate the average of all integers in a dictionary.
    
    Args:
        d (dict): A dictionary where each key corresponds to either a single integer or a list of integers.
    
    Returns:
        float: The average of all integers in the dictionary.
    """
    total = 0  # Total sum of all integers
    count = 0  # Count of all integers

    for k, v in d.items():
        if isinstance(v, list):
            total += sum(v)
            count += len(v)
        else:
            total += v
            count += 1

    return total / count