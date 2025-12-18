"""
QUESTION:
Write a function named `findWords` that takes a list of strings `words` as input and returns a list of words that can be typed using only the letters present on a single row of the American keyboard. The returned words should be in the order of the keyboard rows they belong to, starting from the top row to the bottom row. The keyboard rows are composed of the following characters: 
- Top row: "qwertyuiop"
- Middle row: "asdfghjkl"
- Bottom row: "zxcvbnm"

The input list `words` will contain 1 to 20 strings, each string will be composed of 1 to 100 English alphabets (both lowercase and uppercase).
"""

def findWords(words):
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    res_top_row = []
    res_middle_row = []
    res_bottom_row = []

    for word in words:
        if set(word.lower()) <= set(keyboard[0]):
            res_top_row.append(word)                    
        elif set(word.lower()) <= set(keyboard[1]):
            res_middle_row.append(word)
        elif set(word.lower()) <= set(keyboard[2]):
            res_bottom_row.append(word)
 
    return res_top_row + res_middle_row + res_bottom_row