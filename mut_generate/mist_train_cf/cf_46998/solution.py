"""
QUESTION:
Implement a function `sorted_merge(A, B)` that takes two sorted lists `A` and `B` as input and returns a new sorted list containing all elements from both lists. The function should compare the first elements of `A` and `B`, append the smaller one to the result list, and remove it from its original list. This process should continue until one of the lists is empty, at which point the remaining elements from the non-empty list should be appended to the result list. Note that the input lists are not modified.
"""

def sorted_merge(A, B):
    result = []
    while A and B:
        if A[0] <= B[0]:
            result.append(A.pop(0))
        else:
            result.append(B.pop(0))

    result.extend(A)
    result.extend(B)
    return result