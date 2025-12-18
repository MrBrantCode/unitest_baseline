"""
QUESTION:
Mobile Display Keystrokes

Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?
Well, here you have to calculate how much keystrokes you have to do for a specific word.

This is the layout:



Return the amount of keystrokes of input str (! only letters, digits and special characters in lowercase included in layout without whitespaces !)

e.g:


mobileKeyboard("123") => 3 (1+1+1)
mobileKeyboard("abc") => 9 (2+3+4)
mobileKeyboard("codewars") => 26 (4+4+2+3+2+2+4+5)
"""

def calculate_keystrokes(word: str) -> int:
    lookup = {c: i for s in '1,2abc,3def,4ghi,5jkl,6mno,7pqrs,8tuv,9wxyz,*,0,#'.split(',') for (i, c) in enumerate(s, start=1)}
    return sum((lookup[c] for c in word))