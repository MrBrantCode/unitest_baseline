"""
QUESTION:
Create a function called `convert_to_italics(sentence)` that takes a string sentence as input. The function should find all occurrences of the word 'bold' in the sentence and replace them with the word 'bold' wrapped in HTML italics tags (<i>bold</i>). The function should return the modified sentence.
"""

def convert_to_italics(sentence):
    # Find the index of the word 'bold' in the sentence
    index = sentence.find('bold')
    
    # Replace 'bold' with the corresponding HTML tag for italics
    if index != -1:
        new_sentence = sentence[:index] + '<i>' + sentence[index:index+4] + '</i>' + sentence[index+4:]
    else:
        new_sentence = sentence
    
    return new_sentence