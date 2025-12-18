"""
QUESTION:
Write a Python function `find_common_items(arr1, arr2)` that takes two parameters, `arr1` and `arr2`, and returns a list of common items between the two arrays. The function should not use any built-in functions or libraries to find the common items, instead using basic programming constructs such as loops and conditionals. Additionally, the function should not modify the original arrays and should handle cases where one or both of the inputs are not valid arrays (i.e., strings).
"""

def find_common_items(arr1, arr2):
    # Check if either of the arrays is a string
    if isinstance(arr1, str) or isinstance(arr2, str):
        return []

    common_items = []
    
    # Iterate through each element in the first array
    for item in arr1:
        # Check if the element is present in the second array
        if item in arr2:
            common_items.append(item)
    
    return common_items