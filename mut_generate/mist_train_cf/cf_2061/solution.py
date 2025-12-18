"""
QUESTION:
Create a function named `reverse_multiline` that takes a multiline string as input, reverses the order of lines, removes leading and trailing whitespace from each line, reverses each line, and handles empty lines and lines containing only whitespace.
"""

def reverse_multiline(message):
    lines = message.split('\n')  
    reversed_lines = []

    for line in lines:
        line = line.strip()  
        if line:
            reversed_line = line[::-1]  
            reversed_lines.append(reversed_line)

    reversed_message = '\n'.join(reversed_lines[::-1])  
    return reversed_message