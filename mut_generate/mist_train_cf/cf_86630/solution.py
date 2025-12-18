"""
QUESTION:
Create a function called `find_elements` that takes two parameters: `array` and `key`, where `array` is a list of lowercase alphabetical characters and `key` is a single lowercase alphabetical character. The function should return a dictionary containing all elements from the `array` whose frequency is equal to the frequency of `key`. If the `array` is empty or the `key` is not found in the `array`, return an empty dictionary. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the `array`.
"""

def find_elements(array, key):
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