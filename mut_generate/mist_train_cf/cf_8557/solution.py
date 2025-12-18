"""
QUESTION:
Implement a function `compress_string(s)` that compresses a string `s` by counting consecutive occurrences of each character and storing it as a tuple with the character and its count. The function should not use any built-in functions or methods for string manipulation or counting, and should not use any additional data structures such as dictionaries or lists to store intermediate results.
"""

def compress_string(s):
    if not s:
        return ""

    compressed = ""
    prev_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            compressed += "(" + prev_char + "," + str(count) + ")"
            prev_char = s[i]
            count = 1

    compressed += "(" + prev_char + "," + str(count) + ")"
    return compressed