"""
QUESTION:
Write a function that returns the index of the first occurence of the word "Wally".  "Wally" must not be part of another word, but it can be directly followed by a punctuation mark.  If no such "Wally" exists, return -1.


Examples:

"Wally" => 0

"Where's Wally" => 8

"Where's Waldo" => -1

"DWally Wallyd .Wally" => -1

"Hi Wally." => 3

"It's Wally's." => 5

"Wally Wally" => 0

"'Wally Wally" => 7
"""

from re import compile

def find_wally_index(string: str) -> int:
    """
    Returns the index of the first occurrence of the word "Wally" in the given string.
    "Wally" must not be part of another word, but it can be directly followed by a punctuation mark.
    If no such "Wally" exists, returns -1.

    :param string: The input string to search within.
    :return: The index of the first occurrence of "Wally" or -1 if not found.
    """
    pattern = compile(r"(^|.*[\s])(Wally)([\.,\s']|$)")
    match = pattern.match(string)
    return match.start(2) if match else -1