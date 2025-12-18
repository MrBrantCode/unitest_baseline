"""
QUESTION:
Implement a function `find_chars(phrase)` that identifies and returns the locations of the letters 'j' and 'a' in a given phrase. The phrase is a string of 1 to 10,000 characters. The function should return a list of dictionaries, where each dictionary contains a character ('j' or 'a') and a list of its corresponding locations in the phrase. Do not use built-in string functions.
"""

def find_chars(phrase):
    locations = ({'char': 'j', 'locations': []}, {'char': 'a', 'locations': []})
    for num, char in enumerate(phrase):
        if char == 'j':
            locations[0]['locations'].append(num)
        elif char == 'a':
            locations[1]['locations'].append(num)
    return locations