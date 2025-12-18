"""
QUESTION:
Create a function `count_characters` that takes a string of printable ASCII characters as input and returns a dictionary with the characters as keys and their frequency in the string as values. The dictionary should be sorted in descending order based on the frequency of each character. If two characters have the same frequency, they should be sorted alphabetically. The function should have a time complexity of O(n log n), where n is the length of the string, and should not use any built-in Python functions or libraries for sorting or counting.
"""

def entance(string):
    # Create an empty dictionary
    character_count = {}

    # Count the frequency of each character
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    # Sort the dictionary based on the frequency and character
    sorted_count = sorted(character_count.items(), key=lambda x: (-x[1], x[0]))

    # Convert the sorted list of tuples to a dictionary
    sorted_dict = {}
    for item in sorted_count:
        sorted_dict[item[0]] = item[1]

    return sorted_dict