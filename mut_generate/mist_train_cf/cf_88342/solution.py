"""
QUESTION:
Write a recursive function `count_occurrences` that takes a jagged array of strings, a target string, and a length threshold as parameters. The function should count the occurrences of the target string in the sub-arrays that have a length greater than the given threshold. It should return the total count of occurrences. The function should include at least two base cases: one for an empty array and one for sub-arrays with a length less than or equal to the threshold.
"""

def count_occurrences(arr, target, lengthThreshold):
    count = 0  

    if len(arr) == 0:
        return 0

    if len(arr[0]) <= lengthThreshold:
        return count_occurrences(arr[1:], target, lengthThreshold)

    for element in arr[0]:
        if element == target:
            count += 1

    count += count_occurrences(arr[1:], target, lengthThreshold)

    return count