"""
QUESTION:
Create a function `reverseMatchingElements` that takes two arrays of integers as input. The function should return an array of integers that are present in both input arrays, but in the reverse order of their appearance in the second array. The function should ignore any duplicate elements in both arrays and only consider the first occurrence. If there are no elements in the second array that match the elements in the first array, the function should return an empty array.
"""

def reverseMatchingElements(array1, array2):
    # Create a set to store the unique elements in array2 in reverse order
    unique_elements = set()

    # Iterate through array2 in reverse order
    for i in range(len(array2)-1, -1, -1):
        # Check if the element is not already in the set and is also present in array1
        if array2[i] not in unique_elements and array2[i] in array1:
            # Add the element to the set
            unique_elements.add(array2[i])

    # Create a list to store the elements in the desired order
    result = []

    # Iterate through array1
    for i in range(len(array1)):
        # Check if the element is in the set
        if array1[i] in unique_elements:
            # Add the element to the list
            result.append(array1[i])

    # Return the result
    return result