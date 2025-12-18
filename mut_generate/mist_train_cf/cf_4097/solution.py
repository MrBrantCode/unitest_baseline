"""
QUESTION:
Write a function `format_text(text, indentation)` that takes a string `text` and an integer `indentation` as input, formats the text by removing all consecutive duplicate characters and applying the given indentation level, and returns a tuple containing the formatted text and a dictionary with the count of each character in the formatted text. The function should have a time complexity of O(n), where n is the length of the text, and a space complexity of O(1), excluding the space required for the output.
"""

def entance(text, indentation):
    formatted_text = ''
    count = {}
    prev_char = ''
    consecutive_count = 0

    for char in text:
        if char != prev_char:
            formatted_text += char
            prev_char = char
            consecutive_count = 1
        else:
            consecutive_count += 1

        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    formatted_text = '\n' + ' ' * indentation + formatted_text.replace('\n', '\n' + ' ' * indentation)

    return formatted_text, count