"""
QUESTION:
Create a function named `count_whitespaces` that takes an input string `input_text`. The function should count the frequency of each type of Unicode whitespace character in the input string and return a dictionary where each key-value pair represents the type of whitespace and its frequency respectively. The dictionary should be sorted in decreasing order of frequency and in case of a tie, the type of whitespace with the lower Unicode value of its corresponding character should be placed first. The function should be able to handle input strings of up to 10^6 characters efficiently. 

The function should use the following mapping for the types of whitespace characters: 
- '\t': 'tab', 
- '\n': 'line feed', 
- '\r': 'carriage return', 
- '\f': 'form feed', 
- '\v': 'vertical tab', 
- ' ': 'space', 
- '\u00A0': 'non-breaking space', 
- '\u1680': 'ogham space mark', 
- '\u180E': 'mongolian vowel separator', 
- '\u2000': 'en quad', 
- '\u2001': 'em quad', 
- '\u2002': 'en space', 
- '\u2003': 'em space', 
- '\u2004': 'three-per-em space',
- '\u2005': 'four-per-em space',
- '\u2006': 'six-per-em space',
- '\u2007': 'figure space',
- '\u2008': 'punctuation space',
- '\u2009': 'thin space',
- '\u200A': 'hair space',
- '\u200B': 'zero-width space',
- '\u202F': 'narrow no-break space',
- '\u205F': 'medium mathematical space',
- '\u3000': 'ideographic space',
- '\uFEFF': 'zero width no-break space'.
"""

import collections

def count_whitespaces(input_text):
    """
    Count the frequency of each type of Unicode whitespace character in the input string.

    Args:
        input_text (str): The input string.

    Returns:
        dict: A dictionary where each key-value pair represents the type of whitespace and its frequency respectively.
    """
    # Dictionary of Unicode whitespaces
    whitespace_dict = {
        '\t': 'tab', 
        '\n': 'line feed', 
        '\r': 'carriage return', 
        '\f': 'form feed', 
        '\v': 'vertical tab', 
        ' ': 'space', 
        '\u00A0': 'non-breaking space', 
        '\u1680': 'ogham space mark', 
        '\u180E': 'mongolian vowel separator', 
        '\u2000': 'en quad', 
        '\u2001': 'em quad', 
        '\u2002': 'en space', 
        '\u2003': 'em space', 
        '\u2004': 'three-per-em space',
        '\u2005': 'four-per-em space',
        '\u2006': 'six-per-em space',
        '\u2007': 'figure space',
        '\u2008': 'punctuation space',
        '\u2009': 'thin space',
        '\u200A': 'hair space',
        '\u200B': 'zero-width space',
        '\u202F': 'narrow no-break space',
        '\u205F': 'medium mathematical space',
        '\u3000': 'ideographic space',
        '\uFEFF': 'zero width no-break space',
    }

    # Identify all whitespace characters in the input_text
    whitespaces = [whitespace_dict[ch] for ch in input_text if ch in whitespace_dict]

    # Count frequency of each whitespace character
    whitespace_counts = collections.Counter(whitespaces)

    # Sort by decreasing frequency, then by Unicode value of the whitespace character
    sorted_counts = dict(sorted(whitespace_counts.items(), key=lambda item: (-item[1], item[0])))

    return sorted_counts