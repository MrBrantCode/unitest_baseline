"""
QUESTION:
Write a function called `rearrange_array` that takes an array of integers as input and returns a rearranged array where no two consecutive elements are the same. The numbers in the array are unique except possibly for duplicates of the same number. If the array has less than 3 elements, return the original array.
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