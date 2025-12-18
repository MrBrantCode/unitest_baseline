"""
QUESTION:
Write a function `count_vowels(s)` that takes a string `s` as input and returns a dictionary where the keys are vowels ('a', 'e', 'i', 'o', 'u') and the values are the corresponding vowel counts. The function should ignore non-alphabet characters, handle both upper and lower case letters, and return an error message for non-string inputs or empty strings.
"""

def count_vowels(s):
    # Error Handling for non-string data types
    if not isinstance(s, str):
        return "Error: Input should be a string"
    
    # Error Handling for empty strings
    if s == "":
        return "Error: String should not be empty"
    
    # Dealing with both upper and lower case letters
    s = s.lower()
    
    vowels = 'aeiou'
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in s:
        # ignoring non-alphabet characters
        if char.isalpha():
            if char in vowels:
                # increment the count of each vowel
                vowel_count[char] += 1
    
    return vowel_count