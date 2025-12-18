"""
QUESTION:
Write a function called `remove_duplicates_and_sort` that takes a string of words as input and returns a string where all the words are in upper case, duplicates are removed, and the words are sorted in descending order based on their length. Do not use any built-in functions or methods for string manipulation, such as upper(), sort(), or split().
"""

def remove_duplicates_and_sort(s):
    """
    This function takes a string of words as input, converts all words to upper case, removes duplicates, 
    and returns a string where the words are sorted in descending order based on their length.

    Args:
        s (str): The input string.

    Returns:
        str: The resulting string with the described transformations.
    """

    # Convert all words to upper case
    upper_case_string = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                upper_case_string += chr(ord(char) - 32)
            else:
                upper_case_string += char
        else:
            upper_case_string += char

    # Remove duplicate words
    words = []
    current_word = ""
    for char in upper_case_string:
        if char.isalpha():
            current_word += char
        elif current_word:
            if current_word not in words:
                words.append(current_word)
            current_word = ""
    if current_word:
        if current_word not in words:
            words.append(current_word)

    # Sort words in descending order based on length
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) < len(words[j]):
                temp = words[i]
                words[i] = words[j]
                words[j] = temp

    # Generate final result
    return " ".join(words)