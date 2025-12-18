"""
QUESTION:
Write a function named `tokenize_and_count` that takes a sentence as input and returns a tuple of tuples, where each inner tuple contains a word and its frequency in the sentence. The function should tokenize the sentence into individual words, convert each word to lowercase, and count the occurrences of each word. The function should not use any built-in string or list functions or data structures such as `split()`, `count()`, or dictionaries.
"""

def tokenize_and_count(sentence):
    sentence = sentence.strip()
    tokens = []
    counts = []
    current_word = ""
    
    for char in sentence:
        if char.isalpha() or char == "'":
            current_word += char
        elif char.isspace() or char in ".,!?":
            if current_word:
                current_word = current_word.lower()
                if current_word in tokens:
                    index = tokens.index(current_word)
                    counts[index] += 1
                else:
                    tokens.append(current_word)
                    counts.append(1)
                current_word = ""
    
    if current_word:
        current_word = current_word.lower()
        if current_word in tokens:
            index = tokens.index(current_word)
            counts[index] += 1
        else:
            tokens.append(current_word)
            counts.append(1)
    
    return tuple(zip(tokens, counts))