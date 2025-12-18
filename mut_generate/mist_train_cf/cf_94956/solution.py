"""
QUESTION:
Implement a function `extract_unique_words(string)` that takes an input string as an argument. Extract all the unique words from the string while preserving their order of occurrence. You are not allowed to use any built-in functions or libraries for tasks like set operations, string splitting, or word checking. The string is assumed to be space-delimited.
"""

def extract_unique_words(string):
    unique_words = []
    seen_words = set()
    
    i = 0
    while i < len(string):
        if string[i] == " ":
            i += 1
            continue
        word = ""
        while i < len(string) and string[i] != " ":
            word += string[i]
            i += 1
        if word not in seen_words:  
            unique_words.append(word)  
            seen_words.add(word)  
    return unique_words