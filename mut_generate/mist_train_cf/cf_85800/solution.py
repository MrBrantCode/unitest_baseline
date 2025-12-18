"""
QUESTION:
The function enhanced_vowels_count should return the total number of vowels from a given word. It should consider 'y' as a vowel only if it is the last letter of the word and it should disregard the case of the alphabets. The function must also respect non-English and special characters. The input string s can contain any Unicode characters, and the function should handle them correctly.
"""

def enhanced_vowels_count(s):
    """
    This function returns the total number of vowels from a given word. It considers 'y' as a vowel only if it is the last letter of the word and disregards the case of the alphabets. It respects non-English and special characters.
    """
    s = s.lower()
    vowels = "aeiouáéíóúüàèìòùâêîôûäëïöüãẽĩõũ"
    count = sum(1 for char in s if char in vowels)
    if s and s[-1] == "y":
        count += 1

    return count