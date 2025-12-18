"""
QUESTION:
Create a function named common_elements that takes two arrays arr1 and arr2 as input, finds their common elements, removes duplicates, and returns them. The function should have a time complexity of O(nlogn + mlogm) and a space complexity of O(min(n, m)), where n and m are the lengths of arr1 and arr2 respectively.
"""

def common_elements(arr1, arr2):
    arr1.sort()
    arr2.sort()

    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    uniqueElements = set()
    for element in result:
        if element not in uniqueElements:
            uniqueElements.add(element)

    return uniqueElements