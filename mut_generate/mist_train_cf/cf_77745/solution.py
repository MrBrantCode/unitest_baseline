"""
QUESTION:
Write a function 'char_count' that takes a string representing a word as input and returns a dictionary showing the number of vowels, consonants, and special characters in the string. Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' when it is at the end of the given word, consonants are any non-vowel alphabets, and special characters are non-alphabet characters. The function should ignore the case and handle special characters in the given word. The output dictionary should be in the format: {'Vowels': <count>, 'Consonants': <count>, 'Special characters': <count>}.
"""

def char_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count_vowels = 0
    count_consonants = 0
    count_specials = 0
    s = s.lower()

    for i in s:
        if i.isalpha():
            if i in vowels or (i == 'y' and s.endswith('y')):
                count_vowels += 1
            else:
                count_consonants += 1
        else:
            count_specials += 1

    return {'Vowels': count_vowels, 'Consonants': count_consonants, 'Special characters': count_specials}