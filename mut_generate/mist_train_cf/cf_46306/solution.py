"""
QUESTION:
Create a function `word_count(paragraph)` that takes a string `paragraph` as input and returns a dictionary. The dictionary should contain the words in the paragraph as keys, and their occurrence counts as values. The function should be case-insensitive, treating words with different capitalization as the same (e.g., 'the' and 'The' are the same word), and it should ignore trailing punctuation in words.
"""

def word_count(paragraph):
    # Remove punctuation from the paragraph
    cleaned_paragraph = "".join(ch for ch in paragraph if ch not in ('!', '.', ':', ',', ';'))
    
    # Split the paragraph into words and convert to lower case
    words = cleaned_paragraph.lower().split()
    
    # Create a dictionary to count the occurrence of each word
    word_dict = {word: words.count(word) for word in words}

    return word_dict