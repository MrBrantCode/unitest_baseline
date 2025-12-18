"""
QUESTION:
Implement the `count_word_occurrences(text: str, word: str) -> int` function, which will take in the `text` string and the `word` to be searched for. The function should return the number of occurrences of the word in the text string, excluding those inside quoted strings or comments. 

Assume that the text string will be properly formatted, with all quoted strings enclosed in single or double quotes, and all comments preceded by the '#' symbol. Quoted strings may contain escape characters and may span multiple lines. Comments may be present within quoted strings. There will be no nested quotes or comments in the text string.
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