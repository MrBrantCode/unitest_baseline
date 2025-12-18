"""
QUESTION:
Create a function `can_arrange(arr)` that finds the greatest index of an element in the input array `arr` that is not in its correct position in a non-decreasing sequence and the index of the next smaller element that can be swapped with it to potentially fix the sequence. The function should return a dictionary with keys 'index' and 'swap_with'. If no such element is found, return {'index': -1, 'swap_with': -1}. The input array does not contain duplicate values.
"""

def can_arrange(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            for j in range(i+1, len(arr)):
                if arr[j] >= arr[i]:
                    return {'index': i, 'swap_with': j-1}
            return {'index': i, 'swap_with': len(arr)-1}
    return {'index': -1, 'swap_with': -1}