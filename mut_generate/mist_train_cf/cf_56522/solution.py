"""
QUESTION:
Create a function `modify_input(input_line, target_letter, replacement_symbol, occurrence, exception_words)` that takes in a string `input_line`, a character `target_letter`, a character `replacement_symbol`, an integer `occurrence`, and a list of strings `exception_words`. The function should replace every nth occurrence of `target_letter` in `input_line` with `replacement_symbol`, excluding occurrences within words in `exception_words`, and return the modified string.
"""

def modify_input(input_line, target_letter, replacement_symbol, occurrence, exception_words):
    """
    Replaces every nth occurrence of target_letter in input_line with replacement_symbol, 
    excluding occurrences within words in exception_words, and returns the modified string.
    
    Parameters:
    input_line (str): The input string.
    target_letter (str): The character to be replaced.
    replacement_symbol (str): The character to replace with.
    occurrence (int): The occurrence of target_letter to replace.
    exception_words (list): A list of words where target_letter should not be replaced.
    
    Returns:
    str: The modified string.
    """
    words = input_line.split(' ')
    count = 0
    new_words = []
    for word in words:
        new_word = ""
        if word not in exception_words:
            for letter in word:
                if letter == target_letter:
                    count += 1
                    if count % occurrence == 0:
                        new_word += replacement_symbol
                        continue
                new_word += letter
        else:
            new_word = word
        new_words.append(new_word)
    return ' '.join(new_words)