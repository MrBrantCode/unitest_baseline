"""
QUESTION:
Write a function named `linear_search` that takes in a list of elements `arr` and a target value `target` as inputs. The function should return the index of the target value if it exists in the list, and -1 otherwise. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1