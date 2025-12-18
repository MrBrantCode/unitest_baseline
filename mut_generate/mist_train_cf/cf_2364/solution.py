"""
QUESTION:
Write a function `count_vowels(string)` that calculates the total number of vowels in a given string, considering both uppercase and lowercase vowels, while excluding vowels that occur as part of a consonant cluster. The function should run in linear time complexity and should not use any built-in Python functions or libraries for string manipulation or iteration.
"""

def count_vowels(string):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    consonant_cluster = False
    count = 0

    for char in string:
        if char in vowels:
            if not consonant_cluster:
                count += 1
            consonant_cluster = False
        else:
            consonant_cluster = True

    return count