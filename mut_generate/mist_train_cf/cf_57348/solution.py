"""
QUESTION:
Create a function `count_palindromes(text)` that takes a string of text as input, splits it into words, and returns a dictionary containing the unique palindromes found in the text as keys and their respective counts as values. The function should be case-sensitive, treating words with different cases as different words.
"""

def count_palindromes(text):
    words = text.split()
    palindromes = {}
    
    for word in words:
        if word == word[::-1]: 
            if word in palindromes:
                palindromes[word] += 1
            else:
                palindromes[word] = 1
                
    return palindromes