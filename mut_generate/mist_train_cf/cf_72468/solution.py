"""
QUESTION:
Implement a function called `columnar_transposition` that takes two parameters: `text` (the input string to be encoded) and `col` (the number of columns for the transposition). The function should rearrange the characters in the input string based on the columnar transposition cipher method, where the characters are rearranged into groups of `col` characters, then read off in columns. If the length of the input string is not a multiple of `col`, any remaining characters should still be included in the encoded string.
"""

def columnar_transposition(text, col):
    rows = int(len(text)/col)
    
    group = [text[i:i+col] for i in range(0, len(text), col)]
    
    rearrange = [list(i) for i in group]
    
    transposed_text = ''
    for c in range(col):
        for r in range(rows+1):
            try:
                transposed_text += rearrange[r][c]
            except IndexError:
                pass
    return transposed_text