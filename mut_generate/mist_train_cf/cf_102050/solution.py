"""
QUESTION:
Create a function named `count_letters` that takes a string as input and returns a dictionary where the keys are the unique letters in the string (both uppercase and lowercase) and the values are the counts of each letter. The function should ignore non-alphabet characters and handle strings with non-English alphabet characters.
"""

def count_letters(string):
    counts = {}
    for char in string:
        if char.isalpha():
            char = char.lower() 
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts