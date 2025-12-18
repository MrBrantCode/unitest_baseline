"""
QUESTION:
Develop a function `can_arrange` that takes a list of unique integers as input and returns a dictionary with the maximum indexed element which is not greater than the previous item along with the index of the next smallest item that can replace it and potentially correct the sequence. If no such element is present, the output should be {'index': -1, 'swap_with': -1}.
"""

def can_arrange(arr):
    """Fixed function"""
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for j in range(i, len(arr)):
                if arr[j] > arr[i-1]:
                    return {'index': i, 'swap_with': j}
    return {'index': -1, 'swap_with': -1}