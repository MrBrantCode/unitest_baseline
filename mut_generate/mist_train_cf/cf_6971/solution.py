"""
QUESTION:
Implement the `count_word_occurrences(text: str, word: str) -> int` function to find the number of occurrences of a given word in a text string, excluding those inside quoted strings or comments. Assume the text string is properly formatted, with quoted strings enclosed in single or double quotes, and comments preceded by the '#' symbol. 

Consider the following: 
1. Quoted strings may contain escape characters.
2. Quoted strings may span multiple lines.
3. Comments may be present within quoted strings.
No nested quotes or comments are present in the text string.
"""

def count_word_occurrences(text: str, word: str) -> int:
    count = 0
    inside_quote = False
    inside_comment = False
    escape = False
    i = 0
    
    while i < len(text):
        if text[i] == '"':
            if not escape:
                inside_quote = not inside_quote
            escape = False
        elif text[i] == "'":
            if not escape and not inside_quote:
                inside_quote = True
            escape = False
        elif text[i:i+2] == '# ':
            if not inside_quote:
                inside_comment = True
            escape = False
        elif text[i] == '\n':
            inside_comment = False
            escape = False
        elif text[i:i+2] == '\\':
            escape = not escape
        elif not inside_quote and not inside_comment:
            if text[i:].startswith(word) and (i+len(word) == len(text) or not text[i+len(word)].isalnum()):
                count += 1
            escape = False
        
        i += 1
    
    return count