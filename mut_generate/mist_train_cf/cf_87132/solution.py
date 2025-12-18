"""
QUESTION:
Implement a function called `string_compressor` that takes a string as input and returns a compressed version of the string. The function should only include characters with at least 3 consecutive occurrences in the compressed string and maintain the order of characters in the original string. The input string only contains uppercase and lowercase letters and has a maximum length of 10^9 characters. The function should be case-insensitive and should return the original string if the compressed string is not shorter.
"""

def string_compressor(s):
    n = len(s)
    if n <= 2:
        return s

    result = ''
    i = 1
    j = 0
    count = 1

    while i < n:
        if s[i].lower() == s[j].lower():
            count += 1
        else:
            if count >= 3:
                result += s[j].lower() + str(count)
            else:
                result += s[j:i]
            count = 1
            j = i

        i += 1

    if count >= 3:
        result += s[j].lower() + str(count)
    else:
        result += s[j:i]

    if len(result) >= n:
        return s
    else:
        return result