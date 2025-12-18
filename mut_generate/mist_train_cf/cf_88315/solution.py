"""
QUESTION:
Format a given text using a specified indentation level and remove consecutive duplicate characters. Return a tuple containing the formatted text and a dictionary with character counts. 

Function name: format_text
Parameters: text (str), indentation (int)
Restrictions: 
- Time complexity: O(n), where n is the length of the text
- Space complexity: O(1)
"""

def format_text(text, indentation):
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