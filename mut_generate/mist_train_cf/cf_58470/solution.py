"""
QUESTION:
Create a function `remove_consonants` that takes one parameter, a string `sentence`. The function should remove all consonants from the input string, handling both uppercase and lowercase letters. It must also validate the input to ensure it is alphanumeric and return an error message for invalid inputs, including null and special characters. Additionally, the function should return the count of vowels in the sentence before and after removing consonants.
"""

def remove_consonants(sentence):
    if not isinstance(sentence, str):
        return 'Error: Input should be a string'
    if not sentence.isalnum() and sentence != '':
        return 'Error: Input should be alphanumeric'
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    vowel_count_before = sum([1 for char in sentence if char in vowels])
    
    modified_sentence = "".join([char for char in sentence if char in vowels or char.isnumeric()])
    
    vowel_count_after = sum([1 for char in modified_sentence if char in vowels])
    
    return modified_sentence, vowel_count_before, vowel_count_after