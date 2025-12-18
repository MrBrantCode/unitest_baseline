"""
QUESTION:
Write a function `find_duplicates` that takes an array `arr` as input, and returns a list of indices of the first set of exactly three duplicate elements in the array. If no such set exists, return an empty list. The function should handle cases where there are more than three duplicates or multiple sets of three duplicates, and return the indices of the last set of three duplicates encountered.
"""

def find_duplicates(arr):
    count_dict = {}
    duplicate_indices = []
    
    for i in range(len(arr)):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
            if count_dict[arr[i]] == 3:
                duplicate_indices.append(i-2)
                duplicate_indices.append(i-1)
                duplicate_indices.append(i)
            elif count_dict[arr[i]] > 3:
                duplicate_indices = [i-2, i-1, i]
        else:
            count_dict[arr[i]] = 1
    
    return duplicate_indices