"""
QUESTION:
Create a function `sortArrayByName` that sorts an array of objects by the 'name' property in descending order and converts the 'name' property to uppercase. The input array contains at most 1 million objects, each with a 'name' property of at most 100 characters and a positive integer 'age' property. The function should achieve a time complexity of O(n log n) and a space complexity of O(1), without using built-in sorting functions or data structures.
"""

def sortArrayByName(array):
    """
    Sorts an array of objects by the 'name' property in descending order and 
    converts the 'name' property to uppercase.

    Args:
    array (list): A list of dictionaries with 'name' and 'age' keys.

    Returns:
    None: The function modifies the input array in-place.
    """
    def merge(left, right):
        result = []
        while left and right:
            if left[0]['name'].upper() > right[0]['name'].upper():
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    # Convert 'name' property to uppercase and sort the array
    for obj in array:
        obj['name'] = obj['name'].upper()
    array[:] = merge_sort(array)