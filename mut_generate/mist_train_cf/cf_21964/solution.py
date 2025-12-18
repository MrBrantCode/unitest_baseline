"""
QUESTION:
Write a function `string_to_array` that takes a string as input and returns an array of words, where each word is a separate element in the array. The function should use only a single loop and have a time complexity of O(n), where n is the length of the input string.
"""

def string_to_array(string):
    words = []  
    word = ""  

    for char in string:
        if char != " ":
            word += char  
        else:
            if word != "":
                words.append(word)  
                word = ""  

    if word != "":
        words.append(word)  

    return words