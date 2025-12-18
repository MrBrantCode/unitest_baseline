"""
QUESTION:
Write a function `most_frequent_char` that finds the most frequently used character in a given string while ignoring any duplicate characters that occur consecutively. The function should be case-insensitive, handle non-alphabetical characters, and have a time complexity of O(n), where n is the length of the string.
"""

def most_frequent_char(string):
    freq = {}  
    max_freq = 0  
    most_freq_char = ''  

    string = string.lower()

    prev_char = None
    for char in string:
        if char.isalpha():
            if char != prev_char:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            prev_char = char

    for char, count in freq.items():
        if count > max_freq:
            max_freq = count
            most_freq_char = char

    return most_freq_char