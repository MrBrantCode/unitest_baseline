"""
QUESTION:
Write a function `categorize_words` that takes a list as input and categorizes the string elements into unigrams (single word) and bigrams (pair of two words). The function should ignore non-string elements and special characters. It should return four values: a list of unigrams, a list of bigrams, the average length of unigrams, and the average length of bigrams (ignoring spaces). The function should handle potential exceptions arising from non-string elements and calculate the average lengths separately for unigrams and bigrams.
"""

def categorize_words(mixed_list):
    """
    Categorize the string elements in a list into unigrams and bigrams.
    
    Args:
    mixed_list (list): A list containing mixed data types.
    
    Returns:
    tuple: A tuple containing a list of unigrams, a list of bigrams, 
           the average length of unigrams, and the average length of bigrams.
    """
    unigrams = []
    bigrams = []
    
    for item in mixed_list:
        try:
            # Ignore non-string elements and special characters 
            if not isinstance(item, str) or not item.replace(' ','').isalpha():
                continue
            words = item.split()
            if len(words) == 1:
                unigrams.append(words[0])
            elif len(words) == 2:
                bigrams.append(item)
        except Exception as e:
            print(f'Error encountered: {e}')
            
    avg_len_unigrams = sum(len(word) for word in unigrams) / len(unigrams) if unigrams else 0
    avg_len_bigrams = sum(len(bigram.replace(' ', '')) for bigram in bigrams) / len(bigrams) if bigrams else 0

    return unigrams, bigrams, avg_len_unigrams, avg_len_bigrams