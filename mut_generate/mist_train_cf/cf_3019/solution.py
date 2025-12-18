"""
QUESTION:
Create a function called `extract_substring` that takes a string `sentence`, `start_word`, and `end_word` as parameters. The function should extract the substring between `start_word` and `end_word` from the `sentence`, ensuring that it is at least 10 characters long, contains at least two uppercase letters, and has no repeated characters.
"""

def extract_substring(sentence, start_word, end_word):
    """
    Extract the substring between start_word and end_word from the sentence, 
    ensuring it is at least 10 characters long, contains at least two uppercase letters, 
    and has no repeated characters.

    Args:
        sentence (str): The input sentence.
        start_word (str): The starting word.
        end_word (str): The ending word.

    Returns:
        str or None: The extracted substring if it meets the conditions; otherwise, None.
    """

    # Find the starting and ending indices of the substring
    start_index = sentence.index(start_word) + len(start_word)
    end_index = sentence.index(end_word)

    # Extract the substring
    substring = sentence[start_index:end_index]

    # Check if the substring meets the required conditions
    if (len(substring) >= 10 and 
        sum(1 for c in substring if c.isupper()) >= 2 and 
        len(set(substring)) == len(substring)):
        return substring
    else:
        return None