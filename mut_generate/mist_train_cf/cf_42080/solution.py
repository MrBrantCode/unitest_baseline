"""
QUESTION:
Write a function `insertLineBreaks(text, wlimit)` that takes in a string `text` and an integer `wlimit` representing the width limit for each line. The function should return the modified text with line breaks inserted at appropriate positions to ensure that no line exceeds the specified width limit, assuming the input text contains only printable ASCII characters and that words are separated by whitespace characters (spaces).
"""

def insertLineBreaks(text, wlimit):
    words = text.split()  
    lines = []  
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + (1 if current_line else 0) <= wlimit:  
            if current_line:  
                current_line += " "
            current_line += word  
        else:
            lines.append(current_line)  
            current_line = word  

    if current_line:  
        lines.append(current_line)

    return "\n".join(lines)