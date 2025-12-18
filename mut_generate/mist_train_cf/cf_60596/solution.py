"""
QUESTION:
Create a function named `juxtapose_strings` that takes two string parameters `sentence1` and `sentence2`. The function should return a dictionary containing the alphabetical characters that appear at the same index in both strings, along with their corresponding repetition counts. The function should only consider characters up to the length of the shorter string and ignore non-alphabetical characters.
"""

def juxtapose_strings(sentence1, sentence2):
    """
    This function takes two strings as parameters and returns a dictionary containing 
    the alphabetical characters that appear at the same index in both strings, 
    along with their corresponding repetition counts.

    Args:
        sentence1 (str): The first input string.
        sentence2 (str): The second input string.

    Returns:
        dict: A dictionary with common characters as keys and their repetition counts as values.
    """

    common_chars_dict = {}
    length = min(len(sentence1), len(sentence2))

    for i in range(length):
        if sentence1[i] == sentence2[i]:
            char = sentence1[i]
            if char.isalpha():
                if char in common_chars_dict:
                    common_chars_dict[char] += 1
                else:
                    common_chars_dict[char] = 1

    return common_chars_dict