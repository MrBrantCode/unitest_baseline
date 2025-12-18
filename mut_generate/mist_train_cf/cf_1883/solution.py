"""
QUESTION:
Create a function `max_consecutive_repeating_vowel` that takes a string `s` as input and returns the maximum consecutive repeating vowel in the string, where the vowels are in reverse alphabetical order (u, o, i, e, a) and the maximum length of consecutive repeating vowels is greater than or equal to 4. The function should return the maximum consecutive repeating vowel and its count if such a sequence exists, otherwise return a message indicating that no such sequence exists.
"""

def max_consecutive_repeating_vowel(s):
    """
    This function finds the maximum consecutive repeating vowel in a given string.
    
    The vowels are in reverse alphabetical order (u, o, i, e, a) and the maximum 
    length of consecutive repeating vowels is greater than or equal to 4.
    
    If such a sequence exists, the function returns the maximum consecutive repeating 
    vowel and its count. Otherwise, it returns a message indicating that no such 
    sequence exists.

    Parameters:
    s (str): The input string.

    Returns:
    tuple or str: A tuple containing the maximum consecutive repeating vowel and its 
    count if such a sequence exists, otherwise a message indicating that no such 
    sequence exists.
    """

    max_vowel_count = 0
    current_vowel_count = 0
    max_vowel = ''
    current_vowel = ''

    for c in s:
        if c in 'uoiea':
            if not current_vowel or c == current_vowel[-1]:
                current_vowel += c
                current_vowel_count += 1
            else:
                current_vowel = c
                current_vowel_count = 1

            if current_vowel_count >= 4 and current_vowel_count > max_vowel_count:
                max_vowel_count = current_vowel_count
                max_vowel = current_vowel
        else:
            current_vowel = ''
            current_vowel_count = 0

    if max_vowel_count >= 4:
        return max_vowel, max_vowel_count
    else:
        return "No sequence of consecutive repeating vowels with a length of 4 or more exists."