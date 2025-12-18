"""
QUESTION:
Write a function `count_vowels_and_consonants(string)` to count the occurrences of each vowel (a, e, i, o, u) and consonants in the given string, considering uppercase letters as vowels. The string may contain special characters and punctuation marks. The function should return the total count of all vowels and consonants in the string.

The input string may contain special characters, punctuation marks, and both lowercase and uppercase letters. The output should include the total count of all vowels and consonants and the individual count of each vowel (a, e, i, o, u).
"""

def count_vowels_and_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    cleaned_string = ''.join(c for c in string if c.isalpha())

    vowel_counts = {vowel: 0 for vowel in vowels}
    consonant_count = 0

    for char in cleaned_string:
        if char in vowels:
            vowel_counts[char] += 1
        else:
            consonant_count += 1

    total_vowels = sum(vowel_counts.values())
    total_consonants = consonant_count

    return {
        "total_vowels": total_vowels,
        "vowel_counts": vowel_counts,
        "total_consonants": total_consonants
    }