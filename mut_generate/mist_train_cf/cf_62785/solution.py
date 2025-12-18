"""
QUESTION:
Implement a function `multiply_by_mode_every_5_elements` that takes an array of integers as input. The function should multiply each element in the array by the mode of every set of 5 consecutive elements, processing the array in chunks of 5. If there are fewer than 5 elements left at the end of the array, consider only those elements to calculate the mode. If there are multiple modes in a chunk, use the smallest one. The function should return the modified array.
"""

from collections import Counter

def multiply_by_mode_every_5_elements(array):
    n = len(array)
    for i in range(0, n, 5):
        segment = array[i:i+5]
        mode = Counter(segment).most_common(1)[0][0]
        for j in range(i, min(i+5, n)):
            array[j] *= mode
    return array