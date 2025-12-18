"""
QUESTION:
Implement the `shorten_lines` function, which takes a string `text`, an integer `max_chars_per_line`, and an integer `max_lines` as input, and returns a modified string where each line has a maximum of `max_chars_per_line` characters and the total number of lines does not exceed `max_lines`.
"""

def shorten_lines(text, max_chars_per_line, max_lines):
    lines = text.split('\n')  
    result = []
    for line in lines:
        while len(line) > max_chars_per_line:
            result.append(line[:max_chars_per_line])  
            line = line[max_chars_per_line:]  
        result.append(line)  
        if len(result) >= max_lines:  
            break
    return '\n'.join(result[:max_lines]) 