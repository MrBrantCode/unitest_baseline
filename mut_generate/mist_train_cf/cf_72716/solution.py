"""
QUESTION:
Create a function called `extract_advanced_data` that takes a string `input_string` as an argument. The function should return a dictionary where the keys are unique words divided by commas or colons and the values are their occurrence counts. If the input string does not contain commas or colons, the function should instead return a dictionary with the count of each individual lower-case alphabetic character that has an odd alphabetical index (where 'a' has an index of 0, 'b' has an index of 1, and so on).
"""

def extract_advanced_data(input_string):
    if ',' in input_string:
        split_sequence = input_string.split(',')
        return {word: split_sequence.count(word) for word in set(split_sequence)}  
    elif ':' in input_string:
        split_sequence = input_string.split(':')
        return {word: split_sequence.count(word) for word in set(split_sequence)}
    else:
        odd_indexed_chars = [char for char in input_string if (ord(char) - ord('a')) % 2 == 1]
        return {char: input_string.count(char) for char in set(odd_indexed_chars)}