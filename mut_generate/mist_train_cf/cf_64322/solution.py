"""
QUESTION:
Write a function `word_count` that takes a string of text as input, where the text includes multiple sentences separated by periods (.) or semi-colons (;) and each sentence includes multiple words separated by spaces. The function should return a tuple containing a list of word counts for each sentence and the total word count for the entire text. Assume there are no special characters or numbers, and consider edge cases such as potentially trailing spaces or punctuation at the end of the sentences.
"""

def word_count(text):
    """
    This function takes a string of text as input and returns a tuple containing 
    a list of word counts for each sentence and the total word count for the entire text.
    
    Args:
        text (str): The input text.
    
    Returns:
        tuple: A tuple containing a list of word counts for each sentence and the total word count.
    """
    # split text into sentences using both periods and semicolons
    sentences = text.replace(';', '.').split('.')
    sentence_word_counts = []
    total_word_count = 0
    
    for sentence in sentences:
        if sentence:
            # remove leading/trailing whitespace and split by spaces to find words
            words = sentence.strip().split(' ')
            sentence_word_counts.append(len(words))
            total_word_count += len(words)
    
    return sentence_word_counts, total_word_count