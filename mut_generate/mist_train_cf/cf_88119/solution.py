"""
QUESTION:
Write a function `delete_element` that deletes all occurrences of a given element from a nested array in-place using a recursive approach. The array can have a maximum length of 10^6 elements, maximum depth of 100, and can contain integers within the range of -10^9 to 10^9. The function should not use any built-in functions or data structures and should have a time complexity of O(n), where n is the total number of elements in the array.
"""

def delete_element(arr, element, depth=0):
    if depth > 100:
        return arr
    
    for i in range(len(arr)):
        if type(arr[i]) == list:
            arr[i] = delete_element(arr[i], element, depth+1)
        elif arr[i] == element:
            arr.pop(i)
            return delete_element(arr, element, depth)
    
    return arr