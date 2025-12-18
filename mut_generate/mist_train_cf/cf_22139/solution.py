"""
QUESTION:
Create a function `countVowelElements` that takes an array as input and counts the number of elements that start with a vowel, considering both uppercase and lowercase vowels. The array may contain strings, numbers, or nested arrays. If an element is a nested array, the function should recursively iterate through its elements. The function should print each element that starts with a vowel and return the total count.
"""

def count_vowel_elements(array):
    """
    Counts the number of elements in the array that start with a vowel.
    
    Args:
    array (list): The input array containing strings, numbers, or nested arrays.
    
    Returns:
    int: The total count of elements that start with a vowel.
    """
    count = 0
    for element in array:
        if isinstance(element, list):  # Check if element is a nested array
            count += count_vowel_elements(element)  # Recursively call the function
        elif isinstance(element, str):  # Check if element is a string
            if element[0].lower() in 'aeiou':  # Check if string starts with a vowel
                print(element)  # Print the element
                count += 1  # Increment the count
    return count