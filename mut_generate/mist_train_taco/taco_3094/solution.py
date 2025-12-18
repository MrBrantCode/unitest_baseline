"""
QUESTION:
Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

Input

The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

Output

Output the decoded ternary number. It can have leading zeroes.

Examples

Input

.-.--


Output

012

Input

--.


Output

20

Input

-..-.--


Output

1012
"""

def decode_borze_code(borze_code: str) -> str:
    i = 0
    total = ''
    while i < len(borze_code):
        if borze_code[i] == '.':
            total += '0'
        elif borze_code[i] == '-':
            if i + 1 < len(borze_code) and borze_code[i + 1] == '.':
                total += '1'
            elif i + 1 < len(borze_code) and borze_code[i + 1] == '-':
                total += '2'
            i += 1
        i += 1
    return total