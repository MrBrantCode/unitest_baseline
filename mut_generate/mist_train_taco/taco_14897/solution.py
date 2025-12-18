"""
QUESTION:
# Task
 Timed Reading is an educational tool used in many schools to improve and advance reading skills. A young elementary student has just finished his very first timed reading exercise. Unfortunately he's not a very good reader yet, so whenever he encountered a word longer than maxLength, he simply skipped it and read on.

 Help the teacher figure out how many words the boy has read by calculating the number of words in the text he has read, no longer than maxLength.

 Formally, a word is a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.

# Example

 For `maxLength = 4` and `text = "The Fox asked the stork, 'How is the soup?'"`, the output should be `7`

 The boy has read the following words: `"The", "Fox", "the", "How", "is", "the", "soup".`

# Input/Output


 - `[input]` integer `maxLength`

    A positive integer, the maximum length of the word the boy can read.

    Constraints: `1 ≤ maxLength ≤ 10.`


 - `[input]` string `text`

    A non-empty string of English letters and punctuation marks.


 - `[output]` an integer

    The number of words the boy has read.
"""

import re

def count_readable_words(max_length: int, text: str) -> int:
    """
    Counts the number of words in the text that the boy can read, given a maximum word length.

    Parameters:
    - max_length (int): The maximum length of words the boy can read.
    - text (str): The text containing words and punctuation marks.

    Returns:
    - int: The number of words in the text that the boy can read.
    """
    # Find all words in the text using regex
    words = re.findall(r'\w+', text)
    
    # Count the number of words that are within the max_length
    readable_word_count = sum(1 for word in words if len(word) <= max_length)
    
    return readable_word_count