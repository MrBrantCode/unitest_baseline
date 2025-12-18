"""
QUESTION:
Create a function `reverse_common_elements` that takes two arrays `arr1` and `arr2` as input and returns the elements that are present in both arrays, but in the reverse order of their appearance in `arr2`. The function should not include any duplicate elements from `arr2` if they exist in `arr1` multiple times.
"""

def reverse_common_elements(arr1, arr2):
    common_elements = []
    
    # Iterate over the elements in the second array in reverse order
    for i in range(len(arr2)-1, -1, -1):
        # Check if the element is present in the first array
        if arr2[i] in arr1 and arr2[i] not in common_elements:
            common_elements.append(arr2[i])
    
    return common_elements