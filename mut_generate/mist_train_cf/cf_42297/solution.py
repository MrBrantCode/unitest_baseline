"""
QUESTION:
Implement a function `calculate_fill_percentage(data)` that takes a dictionary `data` as input, where the keys are bin IDs and the values are tuples containing the current fill level and the maximum capacity of the bin. The function should return a new dictionary where the keys are the bin IDs and the values are the calculated fill percentages. If the data for a bin is missing or corrupted (i.e., the current fill level or maximum capacity is `None`), or the maximum capacity is 0, the fill percentage should be considered as 0.
"""

def calculate_fill_percentage(data):
    fill_percentages = {}
    for bin_id, fill_data in data.items():
        if fill_data[0] is not None and fill_data[1] is not None and fill_data[1] != 0:
            fill_percentages[bin_id] = (fill_data[0] / fill_data[1]) * 100
        else:
            fill_percentages[bin_id] = 0
    return fill_percentages