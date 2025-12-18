"""
QUESTION:
Write a function named `median_lists` that takes a list of lists as input, where each sublist contains floating point numbers. The function should return the median value for each sublist as a tuple. If any sublist contains non-numeric data types, the function should return an error message for that specific sublist.
"""

def median_lists(lists):
    medians = []
    for l in lists:
        try:
            sorted_list = sorted([i for i in l if isinstance(i, float) or isinstance(i, int)])
            if not sorted_list:
                medians.append('Error: The list contains non-numeric data types')
                continue
            if len(sorted_list) % 2 == 0:
                medians.append((sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2)
            else:
                medians.append(sorted_list[len(sorted_list) // 2])
        except TypeError:
            medians.append('Error: The list contains non-numeric data types')
    return tuple(medians)