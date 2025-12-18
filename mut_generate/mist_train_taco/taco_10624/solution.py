"""
QUESTION:
You are given a string S. S consists of several words separated by one or more spaces. Word consists of Latin letters as well as other symbols (but not spaces).
In each word which starts from lowercase Latin letter replace starting letter with uppercase Latin letter.

Input
The only line contains S

Output
Output one line with modified string S.

Constraints
1 ≤ length of S ≤ 30 000

SAMPLE INPUT
Wish you were here

SAMPLE OUTPUT
Wish You Were Here
"""

def capitalize_first_letter_of_words(S: str) -> str:
    y = []
    for x in S.split(' '):
        if x and x[0].isalpha() and x[0].islower():
            x = x[0].upper() + x[1:]
        y.append(x)
    return ' '.join(y)