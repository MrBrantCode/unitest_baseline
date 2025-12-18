"""
QUESTION:
**An [isogram](https://en.wikipedia.org/wiki/Isogram)** (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter. It is also used by some to mean a word or phrase in which each letter appears the same number of times, not necessarily just once.

You task is to write a method `isogram?` that takes a string argument and returns true if the string has the properties of being an isogram and false otherwise. Anything that is not a string is not an isogram (ints, nils, etc.)


**Properties:**
 
 - must be a string
 - cannot be nil or empty
 - each letter appears the same number of times (not necessarily just once)
 - letter case is not important (= case insensitive)
 - non-letter characters (e.g. hyphens) should be ignored
"""

from collections import Counter
import re

def is_isogram(word):
    # Check if the input is a string and not empty
    if not isinstance(word, str) or not word:
        return False
    
    # Convert the word to lowercase and remove non-letter characters
    cleaned_word = re.sub('[^a-z]', '', word.lower())
    
    # Count the frequency of each letter
    letter_counts = Counter(cleaned_word).values()
    
    # Check if all letter frequencies are the same
    return len(set(letter_counts)) == 1