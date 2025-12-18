"""
QUESTION:
Create a function called `count_characters` that takes a string as input. The function should return a dictionary containing the alphanumeric characters in the string as keys and their frequency in the string as values. The dictionary should be sorted in descending order based on the frequency of each character. If two characters have the same frequency, they should be sorted alphabetically. The function should ignore any leading or trailing whitespace and punctuation marks in the string, and it should not use any built-in Python functions or libraries for sorting or counting. The function should have a time complexity of O(n log n), where n is the length of the string.
"""

def count_characters(string):
    # Remove punctuation marks
    string = ''.join(char for char in string if char.isalnum())

    # Count the frequencies of each character
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Sort the dictionary in descending order based on frequency and then alphabetically
    sorted_char_freq = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))

    # Convert the sorted list of tuples to a dictionary
    sorted_dict = {}
    for item in sorted_char_freq:
        sorted_dict[item[0]] = item[1]

    return sorted_dict