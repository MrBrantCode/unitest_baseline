"""
QUESTION:
Given a 2D array of integers where each sub-array can have different lengths, write a function `find_unpaired(arr)` that returns a list of tuples. Each tuple contains the index of a sub-array and an unpaired number found in that sub-array. An unpaired number is a number that appears an odd number of times in the sub-array. If no unpaired numbers are found in any sub-array, return an empty list.
"""

def find_unpaired(arr):
    res = []
    for i, subarr in enumerate(arr):
        counts = {}
        for num in subarr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num, count in counts.items():
            if count % 2 != 0:
                res.append((i, num))
                break
    return res