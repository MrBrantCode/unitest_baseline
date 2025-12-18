"""
QUESTION:
Create a function named `extract_unique_words` that takes a string as input. The function should return a list of unique words from the input string, preserving their order of occurrence, without using any built-in functions or libraries for this task. The input string is assumed to be space-separated.
"""

def extract_unique_words(string):
    unique_words = []  
    seen_words = set()  
    
    words = string.split()
    
    for word in words:
        if word not in seen_words:  
            unique_words.append(word)  
            seen_words.add(word)  
    
    return unique_words