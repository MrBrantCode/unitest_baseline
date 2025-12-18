"""
QUESTION:
Implement a function named `split_words` that takes a string `txt` as input. The function should return a list of words separated by either a space or comma if they exist and the words consist only of alphabets. If the string does not contain a space or comma, or if the words contain non-alphabet characters, reconstruct the string to have all lowercase letters and return the count of alternating characters starting from the first character. The count of alternating characters is calculated based on their position in the alphabet (ord('a') = 0, ord('b') = 1, ... ord('z') = 25).
"""

def split_words(txt):
    '''
    Given a string of words, return a list of words separated 
    by either a space or comma. If neither exist, return a count 
    of the lowercase letters with odd indexes (ord('a') = 0, 
    ord('b') = 1, ... ord('z') = 25).

    Furthermore, add functionality where it would check if these 
    words consist of only alphabets. If not, consider that as 
    a case where space or comma doesn't exist. 

    Reconstruct the string to have all lowercase letters and 
    return the count of alternating characters starting from 
    the first character.

    '''
    
    txt = txt.lower()
    
    if (" " in txt) or ("," in txt):
        words = []
        for word in txt.replace(',', ' ').split():
            if word.isalpha():
                words.append(word)
            else:
                return len([ch for i, ch in enumerate(txt) if i % 2 == 0])
        return words
                
    else:
        return len([ch for i, ch in enumerate(txt) if ord(ch) % 2 == 1])