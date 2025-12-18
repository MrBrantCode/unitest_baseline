"""
QUESTION:
Create a function called `count_vowels_consonants` that takes a string input and classifies each character as a vowel, consonant, digit, special character, or space, printing the classification for each character. The function should also return the total counts for each category, handling both uppercase and lowercase characters, non-ASCII characters, and non-alphanumeric characters.
"""

def count_vowels_consonants(input_string):
    """
    Classifies each character in the input string as a vowel, consonant, digit, 
    special character, or space, and returns the total counts for each category.

    Args:
    input_string (str): The input string to be classified.

    Returns:
    dict: A dictionary containing the total counts for vowels, consonants, digits, 
    special characters, and spaces.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_char_count = 0
    space_count = 0

    for char in input_string:
        if char.lower() in vowels:
            print(char, "- Vowel")
            vowel_count += 1
        elif char.isalpha():
            print(char, "- Consonant")
            consonant_count += 1
        elif char.isdigit():
            print(char, "- Digit")
            digit_count += 1
        elif char.isspace():
            print(char, "- Space")
            space_count += 1
        else:
            print(char, "- Special Character")
            special_char_count += 1

    print("Total Vowels:", vowel_count)
    print("Total Consonants:", consonant_count)
    print("Total Digits:", digit_count)
    print("Total Special Characters:", special_char_count)
    print("Total Spaces:", space_count)

    return {
        'vowels': vowel_count,
        'consonants': consonant_count,
        'digits': digit_count,
        'special_chars': special_char_count,
        'spaces': space_count
    }