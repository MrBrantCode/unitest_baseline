"""
QUESTION:
Implement a function called `string_compressor` that takes in a string of uppercase and lowercase letters (maximum length 10^9 characters) and returns a compressed version of the string. The compressed string consists of repeated characters followed by the count of consecutive occurrences, but only includes characters with at least 3 consecutive occurrences. If the compressed string is not shorter than the original string, return the original string. The function should be case-insensitive and maintain the order of characters in the original string.
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