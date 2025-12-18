"""
QUESTION:
Create a function named `find_word` that takes a `sentence` and a `word` as input. The function should return the index of the given word in the sentence. The sentence should contain at least 10 words and should not exceed a maximum length of 100 characters. The word should only be considered a match if it appears as a complete word, not as part of another word. The word should be case-insensitive when comparing with the sentence.
"""

def find_word(sentence, word):
    sentence = sentence.lower()
    word = word.lower()
    words = sentence.split(" ")
    
    for i in range(len(words)):
        if words[i] == word:
            return i
    
    return -1