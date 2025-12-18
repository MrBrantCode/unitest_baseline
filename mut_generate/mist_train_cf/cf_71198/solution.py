"""
QUESTION:
Write a function `convert_first_person_to_third` that takes a string sentence as input, replaces all occurrences of the first person singular pronoun "I" with the third person singular pronoun "He", and updates verb conjugations accordingly. The function should use a predefined dictionary to map first person singular verb forms to their corresponding third person singular forms. Assume the input string is properly space-separated and contains no punctuation. The function should return the modified sentence.
"""

def convert_first_person_to_third(sentence):
    # Define the verb conversion dictionary
    verb_conversion = {
        "am": "is",
        "have": "has",
        "do": "does",
        "plan": "plans",
        "start": "starts"
    }
    
    # Split the sentence into words
    words = sentence.split(' ')
    
    # Traverse the list and replace words as per requirement
    for i in range(len(words)):
        if words[i] == "I":
            words[i] = "He"
        elif words[i] in verb_conversion.keys():
            words[i] = verb_conversion[words[i]]
    
    # Join words to produce final sentence
    return ' '.join(words)