"""
QUESTION:
Design a recursive function `find_all_anagrams` that generates all possible anagrams of a given word and identifies which of these anagrams are the same when reversed. The function should distinguish between upper-case and lower-case letters, not use any anagram-solving libraries or built-in functions, and minimize time complexity.
"""

from collections import defaultdict

def find_all_anagrams(word, anagram=''):
    """
    Recursively generates all possible anagrams of a given word.

    Args:
    word (str): The input word.
    anagram (str): The current anagram being built (default is an empty string).

    Returns:
    list: A list of all possible anagrams.
    """

    # Base Condition
    if len(word) == 0:
        return [anagram]
    
    anagrams = [] # This will store all our anagrams
    
    letter_map = defaultdict(int)
    for letter in word:
        letter_map[letter] += 1
        
    for letter in letter_map.keys():
        
        remaining = word.replace(letter, '', 1)

        anagrams.extend(find_all_anagrams(remaining, anagram + letter))

    return anagrams