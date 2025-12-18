"""
QUESTION:
Create a function called `vector_addition` that takes two 1D arrays `arr1` and `arr2` as input. The function should perform element-wise addition of the two arrays and handle cases where the lengths of the arrays are not equal. If one array is shorter than the other, assume the missing elements are zero. The function should return the resulting array after performing vector addition. The function should not take any other parameters besides `arr1` and `arr2`, and it should not modify the input arrays.
"""

def entance(arr1, arr2):
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