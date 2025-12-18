"""
QUESTION:
Develop a function `avg_max_min` that calculates the average of the five highest and five lowest numbers in a given list without using built-in Python sorting and max/min functions. The function should handle edge cases where the list has less than five elements, in which case it should return an error message.
"""

def avg_max_min(numbers):
    if len(numbers) < 5:
        return 'Cannot perform function on a list with less than five elements.'

    max_vals = []
    min_vals = []
    for i in range(5):
        max_val = None
        min_val = None
        for val in numbers:
            if max_val is None or val > max_val:
                max_val = val
            if min_val is None or val < min_val:
                min_val = val
        max_vals.append(max_val)
        min_vals.append(min_val)
        numbers.remove(max_val)
        numbers.remove(min_val)

    return (sum(max_vals) + sum(min_vals)) / 10.0