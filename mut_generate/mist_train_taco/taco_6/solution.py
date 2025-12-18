"""
QUESTION:
An **anagram** is the result of rearranging the letters of a word to produce a new word.

**Note:** anagrams are case insensitive

Complete the function to return `true` if the two arguments given are anagrams of each other; return `false` otherwise.


## Examples

* `"foefet"` is an anagram of `"toffee"`

* `"Buckethead"` is an anagram of `"DeathCubeK"`
"""

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Determines if two strings are anagrams of each other.

    Args:
        str1 (str): The first string to be checked.
        str2 (str): The second string to be checked.

    Returns:
        bool: True if str1 and str2 are anagrams of each other, False otherwise.
    """
    return sorted(str1.lower()) == sorted(str2.lower())