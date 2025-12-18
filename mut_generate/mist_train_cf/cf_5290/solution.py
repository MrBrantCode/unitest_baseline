"""
QUESTION:
Create a function called `process_sentence(sentence)` that takes a sentence as input. The function should perform the following tasks: 
- Capitalize the first letter of each word, 
- Remove any duplicate words while ignoring case sensitivity, 
- Sort the words in alphabetical order, and 
- Count the number of times each word appears in the sentence, ignoring case sensitivity. 
The function should return three values: the modified sentence with the first letter of each word capitalized, a list of sorted unique words, and a dictionary where the keys are the words and the values are the number of occurrences. 
Assume the input sentence only contains words separated by spaces, and does not contain any punctuation marks or special characters.
"""

def process_sentence(sentence):
    # Capitalize the first letter of each word
    capitalized_sentence = sentence.title()
    
    # Remove any duplicate words
    words = capitalized_sentence.split()
    unique_words = list(set(words))
    
    # Sort the words in alphabetical order
    sorted_words = sorted(unique_words, key=lambda x: x.lower())
    
    # Count the number of times each word appears
    word_count = {}
    for word in words:
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    
    return capitalized_sentence, sorted_words, word_count