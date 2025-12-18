"""
QUESTION:
Create a function `keep_duplicates` that takes an array as input and returns a new array containing only the elements that occur more than once in the input array, with each element appearing the same number of times as in the original array.
"""

def keep_duplicates(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    result = []
    for num, count in counts.items():
        if count > 1:
            for _ in range(count):
                result.append(num)
                
    return result