"""
QUESTION:
Write a function `find_control_characters` that takes a string as input and returns the count of each type of control character (\r, \n, \t) found in the string, along with their respective positions. The function should handle cases with multiple occurrences of the same control character and correctly identify their positions. It should also handle edge cases such as an empty string or a string with no control characters.
"""

def find_control_characters(string):
    control_characters = {
        '\r': 'Carriage returns',
        '\n': 'Line feeds',
        '\t': 'Tabs'
    }
    control_character_counts = {character: 0 for character in control_characters}
    control_character_positions = {character: [] for character in control_characters}
    
    for i, char in enumerate(string):
        if char in control_characters:
            control_character_counts[char] += 1
            control_character_positions[char].append(i)
    
    return control_character_counts, control_character_positions