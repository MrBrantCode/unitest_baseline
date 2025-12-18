"""
QUESTION:
Write a function `remove_middle_word_and_reverse` that takes an input string of words separated by spaces and returns the string with the middle word(s) removed and the remaining words reversed. If the string has an odd number of words, remove the single middle word. If the string has an even number of words, remove the two middle words. The resulting string should be reversed.
"""

def remove_middle_word_and_reverse(input_str):
    """
    This function takes an input string of words separated by spaces, 
    removes the middle word(s), and returns the remaining string reversed.

    If the string has an odd number of words, it removes the single middle word.
    If the string has an even number of words, it removes the two middle words.

    Args:
        input_str (str): The input string of words separated by spaces.

    Returns:
        str: The resulting string with the middle word(s) removed and reversed.
    """

    # Split the string into words
    words = input_str.split()

    # Remove the middle word and join the remaining words.
    if len(words) % 2 == 0:
        # if there is an even number of words, remove the two middle ones
        middle_index = len(words) // 2
        new_str = words[:middle_index - 1] + words[middle_index + 1:]
    else:
        # if there is an odd number of words, remove the middle one
        middle_index = len(words) // 2
        new_str = words[:middle_index] + words[middle_index + 1:]

    # Join the words back into a string
    new_str = ' '.join(new_str)

    # Reverse the string
    reversed_str = new_str[::-1]

    return reversed_str