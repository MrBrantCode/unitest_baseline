"""
QUESTION:
Create a function `find_pairs(array, target)` that takes an array of integers and a target integer as input, and returns all pairs of elements in the array that sum up to the target. The array can contain negative, zero, or positive integers, and the target can be any integer. Each pair should only appear once in the output, with the elements in the pair in any order.
"""

def find_pairs(array, target):
    pairs = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                pairs.append([array[i], array[j]])
    return pairs