"""
QUESTION:
Write a function `consonants_freq(sentence)` that takes a sentence as input and returns a dictionary where the keys are the consonants that start the words in the sentence and the values are their respective frequencies. The function should be case-insensitive, ignore punctuation, and only consider the first character of each word.
"""

def consonants_freq(sentence):
    """
    Returns a dictionary where the keys are the consonants that start the words in the sentence and the values are their respective frequencies.
    
    The function is case-insensitive, ignores punctuation, and only considers the first character of each word.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary where the keys are the consonants and the values are their frequencies.
    """
    
    # Dictionary to store counts of consonants
    freq = {}
    
    # Converting uppercase letters to lowercase and 
    # remove punctuation using translate() method
    s = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Checking each word in the sentence
    for word in s.split():
        letter = word[0]
        if letter in 'aeiou':
            continue
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
                
    return freq