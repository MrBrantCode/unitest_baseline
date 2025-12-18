"""
QUESTION:
Write a Python function named `find_unrelated_word` that determines the word in the third sentence of a given paragraph that is not related to the others. The paragraph and the related words are passed as parameters to the function. The function should return the unrelated word. The word should be compared with the related words after removing punctuation and converting to lowercase. The function should split the paragraph into sentences based on ". ".
"""

def find_unrelated_word(paragraph, related_words):
    """
    This function determines the word in the third sentence of a given paragraph 
    that is not related to the others. The paragraph and the related words are 
    passed as parameters to the function. The function returns the unrelated word.

    Parameters:
    paragraph (str): The input paragraph.
    related_words (set): A set of related words.

    Returns:
    str: The unrelated word.
    """
    # Remove punctuation from related words
    related_words = {word.strip('.,!?"\'').lower() for word in related_words}

    # Split the paragraph into sentences
    sentences = paragraph.split(". ")

    # Check if the paragraph has at least three sentences
    if len(sentences) < 3:
        return None

    # Split the third sentence into words
    words = sentences[2].split()

    # Find the word in the third sentence that is not related
    for word in words:
        word = word.strip('.,!?"\'').lower()
        if word not in related_words:
            return word

    # If all words in the third sentence are related, return None
    return None