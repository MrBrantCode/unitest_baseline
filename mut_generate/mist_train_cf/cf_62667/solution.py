"""
QUESTION:
Implement a function `find_unpaired` that takes a 2D array of integers as input. The function should return a list of integers that appear an odd number of times across all sub-arrays. There are no restrictions on the size of the sub-arrays, and the order of the output list does not matter.
"""

def find_unpaired(lst):
    # create a dictionary to count numbers frequency
    counts = {}
    for sub in lst:
        for num in sub:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

    # find the unpaired numbers
    return [num for num, count in counts.items() if count % 2 != 0]