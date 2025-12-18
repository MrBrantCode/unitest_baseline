"""
QUESTION:
Create a function called `validate_string` that takes a string as an input and returns a boolean value. The input string must meet the following conditions:
- It should have a length of exactly 5.
- It should contain at least two unique vowels.
- It should not have consecutive repeating alphabets.
- If the string contains a number, the number should be prime.

Restrictions:
- The function should handle both alphabets and numbers in the string.
"""

def validate_string(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    unique_vowels = set()
    if len(input_string) != 5:
        return False

    # Check for repeated alphabets
    for i in range(4): 
        if input_string[i] == input_string[i+1]:
            return False

    for char in input_string:
        if char in vowels:
            unique_vowels.add(char)
        if char.isdigit():
            num = int(char)
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return False
            else:
                return False        
    if len(unique_vowels) < 2:
        return False

    return True