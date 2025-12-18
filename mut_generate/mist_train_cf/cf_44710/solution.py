"""
QUESTION:
Create a function named `rotation_array` that generates an array of length N by rotating the elements of a given list by a constant K. The function should take three parameters: `given_list`, `N`, and `K`, and return the rotated array. If `given_list` is empty, return an empty list. The function should handle cases where K exceeds the length of `given_list` by wrapping around to the beginning of the list.
"""

def rotation_array(given_list, N, K):
    if not given_list:
        return []
    rotated_list = []
    len_given_lst = len(given_list)
    for i in range(N):
        rotated_list.append(given_list[(i + K) % len_given_lst])
    return rotated_list