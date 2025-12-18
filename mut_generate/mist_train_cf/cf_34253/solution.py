"""
QUESTION:
Create a function called `mood_mirror` that takes a string input and applies the following rules:
- If the input is a single word, reverse the word.
- If the input is a sentence, reverse the order of the words.
- If the input is a question, prepend the reversed word or sentence with "I'm not sure, but let's find out! ". 
The function should return the modified string based on these rules.
"""

def mood_mirror(input_str):
    if input_str.endswith('?'):
        response = "I'm not sure, but let's find out! "
    else:
        response = ""
    
    words = input_str.strip('?').split()
    if len(words) == 1:
        modified_output = response + words[0][::-1]
    else:
        modified_output = response + ' '.join(words[::-1])
    
    return modified_output