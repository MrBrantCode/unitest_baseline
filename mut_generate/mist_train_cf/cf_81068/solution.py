"""
QUESTION:
Create a function `check_pangram(sentence)` that takes a string `sentence` as input. The function should return "This sentence is a pangram" if the sentence contains all 26 English alphabet letters at least once (case-insensitive), otherwise return a list of missing alphabet letters.
"""

def check_pangram(sentence): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    present_letters = "".join(sorted(set(sentence.lower())))  
    
    alphabet_letters = "" 
    for char in present_letters: 
        if char in alphabet: 
            alphabet_letters += char
    
    if alphabet == alphabet_letters: 
        return "This sentence is a pangram"
    
    missing_letters = [letter for letter in alphabet if letter not in alphabet_letters] 
    
    return missing_letters