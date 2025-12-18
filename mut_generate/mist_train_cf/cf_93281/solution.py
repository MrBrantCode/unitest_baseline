"""
QUESTION:
Write a function named `vector_addition` that takes two 1D arrays `arr1` and `arr2` as input and returns their element-wise sum. If the arrays have different lengths, the shorter array should be padded with zeros from the right to match the length of the longer array.
"""

def vector_addition(arr1, arr2):
    # Get the lengths of the input arrays
    len1 = len(arr1)
    len2 = len(arr2)
    
    # Determine the length of the resulting array
    max_len = max(len1, len2)
    
    # Pad the arrays with zeros to make them equal in length
    arr1 = arr1 + [0] * (max_len - len1)
    arr2 = arr2 + [0] * (max_len - len2)
    
    # Perform vector addition element-wise
    result = [x + y for x, y in zip(arr1, arr2)]
    
    return result