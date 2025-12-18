"""
QUESTION:
Create a function `enhanced_vowel_count` that takes a string `text` as input and returns a dictionary containing two keys: `count` and `most_common`. The `count` key should store the total number of vowel occurrences in the input string, considering 'y' as a semi-vowel and differentiating between uppercase and lowercase vowels. The `most_common` key should store the most frequently occurring vowel (both lower and upper case). If the input string does not contain any vowels, the `most_common` key should be `None`.
"""

from collections import Counter

def enhanced_vowel_count(text: str): 
    vowels = [x for x in text if x.lower() in 'aeiouy']
    vowel_frequency = Counter(vowels)

    most_common = vowel_frequency.most_common(1)
    if len(most_common) == 0:
        most_common = None
    else:
        most_common = most_common[0][0]

    return {'count': sum(vowel_frequency.values()), 'most_common': most_common}