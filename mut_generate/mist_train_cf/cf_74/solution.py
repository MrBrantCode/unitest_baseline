"""
QUESTION:
Create a function called `count_vowels` that takes a string as input. The function should return a dictionary containing the count and positions of each vowel (both lowercase and uppercase) found in the string. The function should ignore non-alphabet characters and spaces, and handle cases where the input string is empty or contains only non-alphabet characters and spaces by returning an empty dictionary.
"""

def count_vowels(string):
    """
    This function takes a string as input and returns a dictionary containing 
    the count and positions of each vowel (both lowercase and uppercase) found 
    in the string. The function ignores non-alphabet characters and spaces, 
    and handles cases where the input string is empty or contains only 
    non-alphabet characters and spaces by returning an empty dictionary.

    Parameters:
    string (str): The input string to be processed.

    Returns:
    dict: A dictionary containing the count and positions of each vowel.
    """

    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowel_positions = {}

    for i, char in enumerate(string):
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in vowels:
                vowels[char_lower] += 1
                if char_lower not in vowel_positions:
                    vowel_positions[char_lower] = []
                vowel_positions[char_lower].append(i)

    return vowel_positions if vowel_positions else {}