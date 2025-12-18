"""
QUESTION:
-----Input-----

The only line of the input contains a 7-digit hexadecimal number. The first "digit" of the number is letter A, the rest of the "digits" are decimal digits 0-9.


-----Output-----

Output a single integer.


-----Examples-----
Input
A278832

Output
0

Input
A089956

Output
0

Input
A089957

Output
1

Input
A144045

Output
1
"""

def check_hex_parity(hex_number: str) -> int:
    """
    Determines the parity of the last digit of a 7-digit hexadecimal number.

    Parameters:
    hex_number (str): A 7-digit hexadecimal number starting with 'A' and followed by decimal digits 0-9.

    Returns:
    int: 0 if the last digit is even, 1 if the last digit is odd.
    """
    if int(hex_number[-1]) % 2 == 0:
        return 0
    else:
        return 1