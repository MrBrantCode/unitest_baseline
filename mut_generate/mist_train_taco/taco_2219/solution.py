"""
QUESTION:
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

```
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def find_anagrams(word: str, words: list) -> list:
    """
    Finds all anagrams of a given word from a list of words.

    Parameters:
    word (str): The word for which to find anagrams.
    words (list): A list of words to check for anagrams.

    Returns:
    list: A list of words that are anagrams of the given word.
    """
    return [item for item in words if sorted(item) == sorted(word)]