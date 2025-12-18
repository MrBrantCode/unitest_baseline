"""
QUESTION:
Create a function named `filter_phrases` that takes three parameters: `phrase_list`, a list of phrases; `consonants`, a list of consonant combinations; and `number_of_vowels`, the target number of vowels. The function should return a list of phrases from `phrase_list` that contain at least one of the given consonant combinations in consecutive order and exactly `number_of_vowels` vowels.
"""

def filter_phrases(phrase_list, consonants, number_of_vowels):
    vowels = 'aeiou'
    filtered_list = []
    for phrase in phrase_list:
        if sum(1 for char in phrase if char.lower() in vowels) == number_of_vowels:
            for consonant in consonants:
                if consonant in phrase.lower():
                    filtered_list.append(phrase)
                    break
    return filtered_list