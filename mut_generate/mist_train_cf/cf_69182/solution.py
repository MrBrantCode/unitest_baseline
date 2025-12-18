"""
QUESTION:
Write a function called `max_and_indices` that finds the maximum number in a list of numbers and returns a tuple containing this maximum value, a list of its corresponding index positions, and the average of these index positions rounded to the nearest integer. The function should handle lists containing duplicate max values.
"""

def max_and_indices(data):
    max_val = data[0]
    indices = []
    for idx, val in enumerate(data):
        if val > max_val:
            max_val = val
            indices = [idx]
        elif val == max_val:
            indices.append(idx)
    avg_index = round(sum(indices)/len(indices))
    return max_val, indices, avg_index