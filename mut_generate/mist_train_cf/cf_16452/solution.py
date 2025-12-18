"""
QUESTION:
Write a function named `longest_substring_with_vowel` that finds the length of the longest substring without repetition in a given string that contains at least one vowel. The vowels are 'a', 'e', 'i', 'o', and 'u'. The function should take one parameter, the input string. The function should return the length of the longest substring without repetition that contains at least one vowel.
"""

def longest_substring_with_vowel(s):
    """
    This function finds the length of the longest substring without repetition 
    in a given string that contains at least one vowel.

    Parameters:
    s (str): The input string.

    Returns:
    int: The length of the longest substring without repetition that contains at least one vowel.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    start = 0
    end = 0
    unique_chars = set()
    max_length = 0
    max_vowel_length = 0

    while end < len(s):
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            end += 1
        else:
            current_length = end - start
            if current_length > max_length:
                if any(char in vowels for char in s[start:end]):
                    max_vowel_length = current_length
                max_length = current_length

            unique_chars.remove(s[start])
            start += 1

    return max_vowel_length