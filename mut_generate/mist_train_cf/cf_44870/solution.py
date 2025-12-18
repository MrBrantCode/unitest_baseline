"""
QUESTION:
Create a function called `can_arrange` that takes an array of unique integers as input and returns a dictionary. The dictionary should contain the index where the array's increasing order is first violated, the index of a smaller element that can be swapped with the element at the index to potentially restore the order, and the total number of swaps needed to rectify the order. If the array is already in increasing order, return a dictionary with `{'index': -1, 'swap_with': -1, 'total_swaps': 0}`.
"""

def can_arrange(arr):
    swaps, candidate, candidate_lexiographical = 0, None, None
    for i in range(len(arr) - 1, 0, -1):
        if arr[i - 1] > arr[i]:
            swaps += 1
            
            if candidate is None or arr[candidate] > arr[i - 1]:
                candidate = i - 1
                candidate_lexiographical = i

            elif arr[i] < arr[candidate]:
                candidate_lexiographical = i

    if candidate is None:
        return {'index': -1, 'swap_with': -1, 'total_swaps': 0}
    else:
        return {'index': candidate, 'swap_with': candidate_lexiographical, 'total_swaps': swaps}