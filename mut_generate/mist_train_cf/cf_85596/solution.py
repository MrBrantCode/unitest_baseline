"""
QUESTION:
Find the unique elements in an array of integers and their positions. Create a function `unique_elements(arr)` that takes a list of integers `arr` as input and returns a dictionary where the keys are the unique elements and their corresponding values are lists of their positions in the array. Assume that the array can contain duplicate integers and the positions are 0-indexed. The solution should have a time complexity of O(n) and space complexity of O(n), where n is the length of the array.
"""

def unique_elements(arr):
    counter = dict()
    for i, num in enumerate(arr):
        if num in counter: 
            counter[num].append(i)
        else:
            counter[num]=[i]

    unique_nums = {key: val for key, val in counter.items() if len(val) == 1}

    return unique_nums