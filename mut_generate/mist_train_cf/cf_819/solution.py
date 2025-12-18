"""
QUESTION:
Create a function `find_elements` that takes two parameters, an array of lowercase alphabetical characters and a lowercase alphabetical character as the object key, and returns a dictionary containing all elements in the array whose value (i.e., the count of occurrences) is the same as the given object key. The function should remove any duplicate values from the array and return an empty dictionary if the array is empty or if the object key is not found in the array. The function should achieve a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.
"""

def find_elements(array, key):
    """
    This function takes an array of lowercase alphabetical characters and a lowercase alphabetical character as the object key.
    It returns a dictionary containing all elements in the array whose value (i.e., the count of occurrences) is the same as the given object key.

    Args:
        array (list): A list of lowercase alphabetical characters.
        key (str): A lowercase alphabetical character.

    Returns:
        dict: A dictionary containing all elements in the array whose value is the same as the given object key.
    """

    # Check if the array is empty
    if len(array) == 0:
        return {}

    # Create a dictionary to store the count of each element in the array
    count = {}

    # Iterate over the array and count the occurrences of each element
    for element in array:
        count[element] = count.get(element, 0) + 1

    # Check if the key is not found in the array
    if key not in count:
        return {}

    # Remove duplicate elements from the array
    array = list(set(array))

    # Create a new dictionary to store the elements whose value is the same as the key
    result = {}

    # Iterate over the array and add the elements whose value is the same as the key to the result dictionary
    for element in array:
        if count[element] == count[key]:
            result[element] = count[element]

    return result