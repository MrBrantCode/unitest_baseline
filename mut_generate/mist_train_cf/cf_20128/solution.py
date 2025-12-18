"""
QUESTION:
Implement a function `modify_string` that takes a string as input, applies the following modifications, and returns the modified string:
- Shift each vowel one position backward in the alphabetical order (e.g., 'a' becomes 'u', 'e' becomes 'a', 'i' becomes 'e', 'o' becomes 'i', and 'u' becomes 'o').
- Shift each consonant one position forward in the alphabetical order (e.g., 'b' becomes 'c', 'c' becomes 'd', and so on).
- Convert the entire string to lowercase.
- Leave non-alphabetical characters unchanged.

The function should not take any additional parameters besides the input string.
"""

def modify_string(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in vowels]

    result = ''
    for char in input_string:
        # Convert the character to lowercase
        char = char.lower()

        # Check if the character is a vowel
        if char in vowels:
            # Find the index of the current vowel in the vowels list
            index = vowels.index(char)
            # Replace the vowel with the previous vowel in the list
            result += vowels[index - 1]
        # Check if the character is a consonant
        elif char in consonants:
            # Find the index of the current consonant in the consonants list
            index = consonants.index(char)
            # Replace the consonant with the next consonant in the list
            result += consonants[(index + 1) % len(consonants)]
        else:
            # Append the character as it is (e.g. spaces, punctuation)
            result += char

    return result