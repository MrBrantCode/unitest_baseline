"""
QUESTION:
Write a function `rearrange_array(arr)` that takes an array of unique integers as input and returns a rearranged version of the array where no two consecutive numbers are the same. The function should handle arrays of any length, including those with less than 3 elements, and there may be multiple valid rearrangements of the same array.
"""

def rearrange_array(arr):
    if len(arr) < 3:
        return arr

    # Count the occurrences of each number in the array
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Sort the numbers in descending order of frequency
    sorted_nums = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

    # Create a new array to store the rearranged elements
    rearranged = [None] * len(arr)

    # Start filling the new array with the most frequent number
    idx = 0
    for num in sorted_nums:
        while counts[num] > 0:
            rearranged[idx] = num
            counts[num] -= 1
            idx += 2
            if idx >= len(arr):
                idx = 1

    return rearranged