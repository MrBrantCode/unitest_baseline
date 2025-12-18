"""
QUESTION:
Create a function `names_with_vowels` that filters a list of names and returns a new list containing only the names that start with a vowel (either uppercase or lowercase). The input list contains strings representing names, and the output should be a list of strings.
"""

def names_with_vowels(names):
    return [name for name in names if name[0].lower() in ['a', 'e', 'i', 'o', 'u']]