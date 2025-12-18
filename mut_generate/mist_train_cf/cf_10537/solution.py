"""
QUESTION:
Create a function `count_vowels` that calculates the total number of vowels in a given string, considering both uppercase and lowercase vowels, and excluding any vowels that occur as part of a consonant cluster. The input string is a sequence of characters and the output should be an integer representing the count of vowels.
"""

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    previous_char = ''
    
    for char in string:
        char = char.lower()
        
        if char in vowels:
            if previous_char in vowels:
                count -= 1
            count += 1
        
        previous_char = char
    
    return count