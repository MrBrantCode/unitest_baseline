"""
QUESTION:
Create a function `create_dictionary(sentence1, sentence2)` that takes two strings `sentence1` and `sentence2` as input and returns a dictionary. The dictionary should contain the alphabetical characters that are present at the same position in both strings, paired with their corresponding repetition counts. The function should be case-insensitive, meaning it treats 'a' and 'A' as the same character. If the sentences are of different lengths, the function should pad the shorter sentence with spaces to make them the same length.
"""

def create_dictionary(sentence1, sentence2):
    # Create empty dictionary
    dictionary = {}
    
    # Ensure both sentences are of the same length
    # If they are not, pad the shorter sentence with spaces
    sentence1 = sentence1.ljust(len(sentence2))
    sentence2 = sentence2.ljust(len(sentence1))

    # Convert sentences to lower case to avoid case sensitivity
    sentence1 = sentence1.lower() 
    sentence2 = sentence2.lower() 

    # Iterate over the characters in the sentences
    for char1, char2 in zip(sentence1, sentence2):
        # If the characters match and are alphabets, add them to the dictionary
        if char1 == char2 and char1.isalpha():
            if char1 in dictionary:
                dictionary[char1] += 1
            else:
                dictionary[char1] = 1
                
    return dictionary