"""
QUESTION:
Create a function named `substitute_article` that takes a string of words as input. The function should replace the first occurrence of the indefinite article "a" or "A" with "the" or "The" respectively, but only if its index is within the first 5 words of the sentence. The function should maintain the original case sensitivity and return the modified string.
"""

def substitute_article(word_string):
    words = word_string.split(" ")
    for i in range(len(words)):
        if i < 5:
            if words[i] == 'a':
                words[i] = 'the'
                break
            elif words[i] == 'A':
                words[i] = 'The'
                break
    
    return ' '.join(words)