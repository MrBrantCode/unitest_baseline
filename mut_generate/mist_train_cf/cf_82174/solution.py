"""
QUESTION:
Implement the function `merge_unique_sorted` that takes two sorted arrays of integers as input and returns a new sorted array containing unique elements from both arrays. The function should achieve this in O(1) extra space and without using any pre-set system functions. The function should not require any additional inputs other than the two input arrays.
"""

def merge_unique_sorted(arr1, arr2):
    i, j = 0, 0
    final = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            final.append(arr2[j])
            j += 1
        else:
            final.append(arr1[i])
            i += 1
            j += 1

    while(i < len(arr1)):
        final.append(arr1[i])
        i += 1

    while(j < len(arr2)):
        final.append(arr2[j])
        j += 1

    final = list(set(final))
    return final