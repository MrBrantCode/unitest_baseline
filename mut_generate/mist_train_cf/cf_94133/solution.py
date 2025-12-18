"""
QUESTION:
Write a function `find_duplicates` that takes an array `A` as input and returns the indices of exactly three duplicate elements if they exist, otherwise an empty list. The function should return the indices of the first three occurrences of the duplicate element. If there are more than three duplicates, the function should still return only the indices of the first three occurrences.
"""

def find_duplicates(A):
    count_dict = {}
    indices_dict = {}
    for i in range(len(A)):
        if A[i] in count_dict:
            count_dict[A[i]] += 1
            indices_dict[A[i]].append(i)
            if count_dict[A[i]] == 3:
                return indices_dict[A[i]][:3]
        else:
            count_dict[A[i]] = 1
            indices_dict[A[i]] = [i]
    return []