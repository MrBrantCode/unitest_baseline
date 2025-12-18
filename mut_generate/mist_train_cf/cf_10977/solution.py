"""
QUESTION:
Create a function called `find_common_elements` that takes two lists, `arr1` and `arr2`, as input and returns their common elements. The function should have a time complexity of O(n+m), where n and m are the lengths of the two arrays, and a space complexity of O(min(n, m)), using additional space proportional to the length of the smaller array.
"""

def find_common_elements(arr1, arr2):
    """
    Returns the common elements of two lists.

    Args:
        arr1 (list): The first list.
        arr2 (list): The second list.

    Returns:
        list: A list of common elements.

    Time complexity: O(n+m), where n and m are the lengths of the two arrays.
    Space complexity: O(min(n, m)), using additional space proportional to the length of the smaller array.
    """

    # If the length of arr1 is greater than the length of arr2, swap the two arrays.
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    # Create an empty dictionary to store the frequency of elements in arr1.
    arr1_elements = {}

    # Iterate through each element in arr1 and store its frequency.
    for element in arr1:
        if element not in arr1_elements:
            arr1_elements[element] = 1
        else:
            arr1_elements[element] += 1

    # Create an empty set to store the common elements.
    common_elements = set()

    # Iterate through each element in arr2 and find the common elements.
    for element in arr2:
        if element in arr1_elements and arr1_elements[element] > 0:
            common_elements.add(element)
            arr1_elements[element] -= 1

    return list(common_elements)