"""
QUESTION:
Write a function called "find_local_maxima" that takes in a list of at least 3 integers and returns a list of tuples, where each tuple contains the index and value of a local maximum in the list. A local maximum is defined as an element in the list that is greater than its immediate neighbors. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1), excluding the space required for the output list.
"""

def find_local_maxima(arr):
    result = []
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            result.append((i, arr[i]))
    return result