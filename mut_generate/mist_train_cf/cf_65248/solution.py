"""
QUESTION:
Given a list of unique integers, create a function named `can_arrange` that returns a dictionary with two keys: 'index' and 'swap_with'. The function should find the largest index of an element that is not less than or equal to the preceding element, and the index of the next smallest element that could be swapped with it to yield a potentially sorted sequence. If no such element exists, return {'index': -1, 'swap_with': -1}.
"""

def can_arrange(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            index = i
            swap_with = -1 
            for j in range(i+1, len(arr)):
                if arr[j] < arr[index]:
                    swap_with = j
            return {'index': index, 'swap_with': swap_with if swap_with != -1 else index + 1}
    return {'index': -1, 'swap_with': -1}