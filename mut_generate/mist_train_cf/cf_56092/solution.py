"""
QUESTION:
Design a function `text_converter(text, case)` that takes a string `text` and a parameter `case` as input. The function should convert the string into snake case notation, treating numbers as separate entities. The `case` parameter should determine the output case, which can be either 'lower', 'upper', or 'camel'.
"""

def text_converter(text, case='lower'):
    snake_text = ''
    for letter in text:
        if letter.isupper():
            snake_text += '_' + letter
        elif letter.isnumeric():
            if snake_text and not snake_text[-1].isnumeric():
                snake_text += '_'
            snake_text += letter
        else:
            snake_text += letter
    snake_text = snake_text.strip('_')
    if case == 'lower':
        return snake_text.lower()
    elif case == 'upper':
        return snake_text.upper()
    elif case == 'camel':
        words = snake_text.split('_')
        return words[0].lower() + ''.join(word.title() for word in words[1:])