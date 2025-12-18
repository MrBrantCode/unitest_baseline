"""
QUESTION:
Write a function named `process_dictionary` that takes a dictionary as input and performs the following tasks:

- Calculate the average of all integer values in the dictionary, assuming they represent ages.
- Return a dictionary containing key-value pairs where the value is a string that follows an alternating pattern of vowels and consonants (considering 'y' as a consonant).

The function should return the calculated average age and the new dictionary with the specified key-value pairs.
"""

def process_dictionary(dictionary):
    def is_alternating(word):
        vowels = 'aeiouAEIOU'
        last_is_vowel = None
        for char in word:
            current_is_vowel = char in vowels
            if last_is_vowel is None:
                last_is_vowel = current_is_vowel
            elif current_is_vowel == last_is_vowel:
                return False
            else:
                last_is_vowel = current_is_vowel
        return True

    ages = []
    new_dictionary = {}
    
    for key, value in dictionary.items():
        if isinstance(value, int):
            ages.append(value)
        elif isinstance(value, str) and is_alternating(value):
            new_dictionary[key] = value
                        
    average_age = sum(ages) / len(ages) if ages else 0  # to avoid division by zero
    
    return average_age, new_dictionary