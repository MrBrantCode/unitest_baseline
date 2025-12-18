"""
QUESTION:
Implement the `insertion_sort` function to sort a list of strings in descending order based on the length of each string. If two strings have the same length, they should be sorted in lexicographical order. The function should not be modified in terms of its signature, and it can be assumed that the input list will only contain strings.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (len(arr[j]) < len(key) or (len(arr[j]) == len(key) and arr[j] < key)):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        
    return arr