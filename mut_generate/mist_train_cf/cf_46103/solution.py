"""
QUESTION:
Write a function called `split_into_sentences` that takes a string as input, breaks it into sentences using the `.split()` function, and returns a dictionary where each key is the sentence order (starting from 1) and each value is another dictionary containing the sentence and its word count. The function should handle punctuation marks '!' and '?' as sentence delimiters, in addition to '.'.
"""

def split_into_sentences(text):
    """
    Breaks the input string into sentences and returns a dictionary with sentence order and details.

    Args:
        text (str): The input string to be split into sentences.

    Returns:
        dict: A dictionary where each key is the sentence order (starting from 1) and each value is another dictionary containing the sentence and its word count.
    """
    sentences = dict()
    split_text = text.replace('!', '.').replace('?', '.').split('.')
    for i, s in enumerate(split_text):
        if s: 
            sentences[i+1] = {'sentence': s.strip(), 'word_count': len(s.split())}
    return sentences