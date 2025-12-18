"""
QUESTION:
Create a function named `capitalize_sentence` that takes a sentence as an argument and returns the formatted sentence with the first letter of each word capitalized. The function should handle sentences that start with a number or special character, as well as sentences that end with a period, exclamation mark, or question mark. It should also handle special characters within words and consider consecutive letters as part of a word.
"""

def capitalize_sentence(sentence):
    """
    Capitalize the first letter of each word in a sentence.

    The function handles sentences that start with a number or special character, 
    as well as sentences that end with a period, exclamation mark, or question mark. 
    It also handles special characters within words and considers consecutive letters as part of a word.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    str: The formatted sentence with the first letter of each word capitalized.
    """
    formatted_sentence = ''
    words = sentence.split()
    for i in range(len(words)):
        word = words[i]
        if word[0].isalnum():
            word = word[0].upper() + word[1:]
        formatted_sentence += word + ' '
    formatted_sentence = formatted_sentence.strip()
    formatted_sentence = formatted_sentence.replace(" . ", ". ")
    formatted_sentence = formatted_sentence.replace(" ! ", "! ")
    formatted_sentence = formatted_sentence.replace(" ? ", "? ")
    return formatted_sentence