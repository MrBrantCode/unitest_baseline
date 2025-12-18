"""
QUESTION:
Implement a function `remove_duplicates_and_shift(s)` that takes a string `s` containing all printable ASCII characters, removes duplicates, and returns a new string. For each character that was duplicated, increase the ASCII value of the next non-duplicated character by the number of times the previous character was duplicated. If the increased ASCII value exceeds the ASCII value of the tilde (~), wrap around and start from space ASCII value (' ', ASCII value 32).
"""

def remove_duplicates_and_shift(s):
    counts = {}
    shift_amount = 0
    new_str = ''
    i = 0
    while i < len(s):
        char = s[i]
        if char not in counts or counts[char] == 0:
            counts[char] = 1
            if shift_amount > 0:
                new_char = chr(((ord(char) - 32 + shift_amount) % 95) + 32)
                new_str += new_char
                shift_amount = 0
            else:
                new_str += char
        else:
            counts[char] += 1
            shift_amount += 1
        i += 1
    return new_str