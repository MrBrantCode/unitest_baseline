"""
QUESTION:
Create a function `longest_characters(string)` that takes a string as input and returns a string containing the longest set of characters in descending order, excluding repeated characters, and including the number of times each character appears in the string. The input string will only contain alphabetical characters (both upper and lower case) and spaces.
"""

def longest_characters(string):
    # remove spaces from the string
    string = string.replace(" ", "")
    
    # convert the string to lowercase
    string = string.lower()
    
    # create a dictionary to store the frequency of characters
    char_freq = {}
    
    # calculate the frequency of each character in the string
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # sort the characters based on their frequency in descending order
    sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    
    # construct the result string
    result = ""
    for char in sorted_chars:
        result += char + str(char_freq[char])
    
    return result