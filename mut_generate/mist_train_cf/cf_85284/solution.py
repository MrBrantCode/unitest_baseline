"""
QUESTION:
Create a function named `reverse_word_letters` that takes a string input and returns a string where the alphabetic characters in each word are reversed, while maintaining the original word and sentence order. The function should handle alphanumeric words and raise an error if the input is not a string.
"""

def reverse_word_letters(txt):
    """
    This function takes a string input and returns a string where the alphabetic characters 
    in each word are reversed, while maintaining the original word and sentence order.

    Args:
        txt (str): The input string.

    Returns:
        str: A string where the alphabetic characters in each word are reversed.

    Raises:
        AssertionError: If the input is not a string.
    """
    try:
        assert isinstance(txt, str)
    except AssertionError:
        return "ERROR: Input must be a string."

    word_list = txt.split(' ')
    reversed_word_list = [''.join(reversed([char for char in word if char.isalpha()])) if word.isalpha() 
                          else ''.join([char if not char.isalpha() else list(word)[index] for index, char in enumerate(reversed(word))])
                          for word in word_list]
    return ' '.join(reversed_word_list)