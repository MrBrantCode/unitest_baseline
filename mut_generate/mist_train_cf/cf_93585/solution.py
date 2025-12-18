"""
QUESTION:
Write a function called `count_letter` that takes two parameters: `string` and `letter`. The function should return the count of occurrences of the `letter` in the `string` (ignoring case sensitivity) along with the indices at which the `letter` appears in the `string`. The `letter` can be a single character or a substring. The function should be able to handle alphanumeric characters, spaces, and special characters in the `string`.
"""

def count_letter(string, letter):
    """
    This function returns the count of occurrences of the letter in the string 
    (ignoring case sensitivity) along with the indices at which the letter appears 
    in the string.

    Args:
        string (str): The input string.
        letter (str): The letter to be searched in the string.

    Returns:
        tuple: A tuple containing the count of occurrences and a list of indices.
    """
    
    string = string.lower()
    letter = letter.lower()

    count = 0
    indices = []
    index = 0

    while True:
        index = string.find(letter, index)
        if index == -1:
            break
        count += 1
        indices.append(index)
        index += len(letter)

    return count, indices