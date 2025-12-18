"""
QUESTION:
Create a function `count_word_occurrences` that takes two parameters: a string `myString` and a word. The function should return the number of times the word appears in the string, considering only sequences of consecutive lowercase alphabetical characters. The function should be case-sensitive and have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). If the word is not found, the function should return -1.
"""

def count_word_occurrences(myString, word):
    count = 0
    word_length = len(word)
    i = 0
    
    while i < len(myString):
        if myString[i].islower():
            j = 0
            while j < word_length and i + j < len(myString) and myString[i + j].islower():
                if myString[i + j] != word[j]:
                    break
                j += 1
            
            if j == word_length:
                count += 1
                i += word_length
            else:
                i += 1
        else:
            i += 1
    
    if count > 0:
        return count
    else:
        return -1