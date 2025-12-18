"""
QUESTION:
Write a function `get_highest_peak(data)` that takes a list of tuples, where each tuple contains the name of a mountain range and its highest peak height. The function should return the tuple containing the name of the mountain range and the peak that is the highest in the world, ignoring any invalid data. The function should handle potential errors such as incorrect data types, missing data, and non-numeric peak heights. The function should return `None` if all tuples are invalid or the data list is empty. The name should be a string and the height should be a positive number.
"""

def get_highest_peak(data):
    max_data = None
    max_height = 0

    for item in data:
        # checks tuple length and height is a number
        if type(item) not in (list, tuple) or len(item) != 2 or not isinstance(item[1], (int, float)):
            continue

        name, height = item
        if type(name) != str or height <= 0:  # checks name is a string and height is positive
            continue

        if height > max_height:
            max_data = item
            max_height = height

    return max_data