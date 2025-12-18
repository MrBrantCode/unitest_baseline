"""
QUESTION:
Create a function named `get_nicknames` that takes a list of character names from the Lord of the Rings as input and returns a list of their corresponding nicknames in alphabetical order. The function should have a time complexity of O(n), where n is the number of characters in the input list, and it should handle duplicate characters by only including each nickname once in the output list.
"""

def get_nicknames(characters):
    nickname_map = {
        "Frodo": "Hobbit",
        "Gandalf": "Wizard",
        "Legolas": "Elf",
        # Add more mappings here if needed
    }
    
    nicknames = set()
    for character in characters:
        if character in nickname_map:
            nicknames.add(nickname_map[character])
    
    return sorted(list(nicknames))