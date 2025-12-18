"""
QUESTION:
Create a function named `last_k_unique_elements` that takes an array and a positive integer K as input, where K is less than or equal to the length of the array. The function should return the last K unique elements of the array in their original order, ignoring any duplicate elements. The function should have a time complexity of O(K) and a space complexity of O(K).
"""

def last_k_unique_elements(arr, K):
    unique_elements = []
    element_count = {}

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] not in element_count:
            unique_elements.append(arr[i])
            element_count[arr[i]] = 1

        if len(unique_elements) == K:
            break

    return unique_elements[::-1]