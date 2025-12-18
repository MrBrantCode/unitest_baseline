"""
QUESTION:
-----Input-----

The input consists of a single string of uppercase letters A-Z. The length of the string is between 1 and 10 characters, inclusive.


-----Output-----

Output "YES" or "NO".


-----Examples-----
Input
GENIUS

Output
YES

Input
DOCTOR

Output
NO

Input
IRENE

Output
YES

Input
MARY

Output
NO

Input
SMARTPHONE

Output
NO

Input
REVOLVER

Output
YES

Input
HOLMES

Output
NO

Input
WATSON

Output
YES
"""

def check_string_pattern(input_string: str) -> str:
    def char_to_index(c: str) -> int:
        return ord(c) - ord('A')

    if len(input_string) <= 2:
        return 'YES'

    a = char_to_index(input_string[0])
    b = char_to_index(input_string[1])

    for i in range(2, len(input_string)):
        c = char_to_index(input_string[i])
        if (a + b) % 26 != c:
            return 'NO'
        a, b = b, c

    return 'YES'