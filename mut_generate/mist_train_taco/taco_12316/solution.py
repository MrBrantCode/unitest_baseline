"""
QUESTION:
-----Input-----

The only line of the input is a string of 7 characters. The first character is letter A, followed by 6 digits. The input is guaranteed to be valid (for certain definition of "valid").


-----Output-----

Output a single integer.


-----Examples-----
Input
A221033

Output
21

Input
A223635

Output
22

Input
A232726

Output
23
"""

def calculate_output(input_string: str) -> int:
    ans = 1
    skip = 0
    for i in range(1, 7):
        if skip:
            skip = 0
            continue
        if i + 1 < 7 and input_string[i] == '1' and input_string[i + 1] == '0':
            ans += 10
            skip = 1
        else:
            ans += ord(input_string[i]) - ord('0')
    return ans