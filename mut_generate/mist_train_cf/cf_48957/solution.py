"""
QUESTION:
Design a function `count_unique_elements` that accepts an array of integers and returns an array containing the count of each unique element, sorted by the element's value in ascending order. The count should exclude elements that appear more than twice in the array.
"""

def count_unique_elements(nums):
    counts = {}
    result = []

    # Count the frequency of each unique number
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Filter out numbers that appear more than twice, sort, and add to result
    for num, count in sorted(counts.items()):
        if count <= 2:
            result += [num] * count

    return result