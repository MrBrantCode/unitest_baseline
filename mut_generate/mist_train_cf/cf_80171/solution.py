"""
QUESTION:
Write a function `unique_words` that takes a string `text` as input. The function should return a list of unique words from the string that have a frequency of occurrence greater than 1 and a length of 4 or more characters. The list should be in alphabetical order.
"""

def unique_words(text):
    """
    Returns a list of unique words from the input string that have a frequency of occurrence greater than 1 and a length of 4 or more characters.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    list: A list of unique words that meet the specified conditions, in alphabetical order.
    """
    # Removing punctuations, converting to lowercase and splitting the text into words
    words = text.replace(".","").lower().split(" ")
    
    # Finding unique words with frequency greater than 1
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    
    # Finding words with more than 3 characters
    result_words = sorted([word for word, freq in word_freq.items() if len(word) > 3 and freq > 1])
    
    return result_words