"""
QUESTION:
Create a function named `convert_to_word_list` that takes a string as input and returns a list of words. The function should exclude punctuation marks, special characters, and numbers from the words, but consider apostrophes as part of the words. The list should be sorted in reverse alphabetical order. If two words have the same reverse alphabetical order, their original order in the string should be reversed. The function should return an empty list if the input string is empty.
"""

def convert_to_word_list(string):
    if not string:
        return []
    
    translation_table = str.maketrans(".,?!;:", "      ")
    string = string.translate(translation_table)
    
    words = string.split()
    words = [word.strip() for word in words]
    
    word_list = []
    for word in words:
        if "'" in word:
            word_list.append(word)
        else:
            word_list.append(''.join(c for c in word if c.isalpha()))
    
    word_list = sorted(word_list, reverse=True)
    
    for i in range(len(word_list) - 1):
        if word_list[i] == word_list[i+1][::-1]:
            word_list[i], word_list[i+1] = word_list[i+1], word_list[i]
    
    return word_list