"""
QUESTION:
Create a function named `find_duplicates` that takes an array `arr` as input and returns the indices of exactly three duplicate elements if they exist, otherwise returns an empty list. The function should handle cases where there are more than three duplicates of the same element.
"""

def find_duplicates(arr):
    count_dict = {}
    indices_dict = {}
    for i in range(len(arr)):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
            indices_dict[arr[i]].append(i)
            if count_dict[arr[i]] == 3:
                return indices_dict[arr[i]]
        else:
            count_dict[arr[i]] = 1
            indices_dict[arr[i]] = [i]
    return []