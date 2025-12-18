"""
QUESTION:
Write a function called `count_vowels_in_words` that takes a sentence as input and returns a dictionary where the keys are the individual words of the sentence and the values are the number of vowels in the respective word. The function should be case-insensitive and should count vowels regardless of their position in the word. The input sentence may contain punctuation.
"""

def count_vowels_in_words(sentence):
    """
    This function takes a sentence as input, splits it into words, 
    and returns a dictionary with the number of vowels in each word.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary where the keys are the individual words 
              and the values are the number of vowels in the respective word.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    word_vowels = {}

    for word in words:
        # Remove punctuation from the word
        word_no_punct = ''.join(e for e in word if e.isalnum())
        vowel_count = sum(1 for letter in word_no_punct.lower() if letter in vowels)
        word_vowels[word_no_punct] = vowel_count

    return word_vowels