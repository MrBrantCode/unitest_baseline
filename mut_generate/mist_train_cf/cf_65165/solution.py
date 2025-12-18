"""
QUESTION:
Write a Python function named `count_letters` that takes a string as input, ignores case sensitivity and special characters, and returns a sorted dictionary with letter counts in descending order. The dictionary should also include the frequency ratio of each letter relative to the total letter count in the sentence. The function should handle potential errors or edge cases such as an empty string or a string with only special characters.
"""

def count_letters(sentence):
    if not isinstance(sentence, str):
        return "Error: Input is not a string"
        
    if len(sentence.strip()) == 0:
        return "Error: Input string is empty or just contains whitespace."

    dict_letters = {}
    total_letters = 0
    
    for char in sentence.lower():
        if char.isalpha():
            total_letters += 1
            if char in dict_letters:
                dict_letters[char][0] += 1
            else:
                dict_letters[char] = [1, 0]
    
    if total_letters == 0:
        return "Error: Input string doesn't contain any alphabets."

    # Calculate frequency ratio
    for k, v in dict_letters.items():
        dict_letters[k][1] = round(v[0] / total_letters, 2)

    # Sort the dictionary by counts in descending order.
    dict_letters = dict(sorted(dict_letters.items(), key=lambda item: item[1][0], reverse=True))
    
    return dict_letters