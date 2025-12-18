"""
QUESTION:
Create a function `delete_element(arr, element)` that deletes all occurrences of `element` from the array `arr` in-place with a time complexity of O(n), without using any extra space.
"""

def delete_element(arr, element):
    index = 0
    for i in range(len(arr)):
        if arr[i] != element:
            arr[index] = arr[i]
            index += 1
    del arr[index:]
    return arr