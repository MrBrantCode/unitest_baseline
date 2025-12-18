"""
QUESTION:
Create a Python function `check_string(s)` that takes a string `s` as input and returns a boolean value indicating whether the string consists solely of English alphabetical characters. If the string is alphabetical, the function should also return a list of tuples, where each tuple contains an alphabetical character and its frequency in the string, sorted in descending order of frequency. If the string is not alphabetical, the function should return a boolean value of False and an error message. The function should not use any in-built Python functions or libraries for data manipulation and sorting.
"""

def check_string(s):
    def is_alpha(c):
        if (('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')):
            return True
        return False

    def to_lower(c):
        if 'A' <= c and c <= 'Z':
            return chr(ord(c) + 32)
        return c

    def sort_freq(freq):
        for i in range(len(freq)):
            for j in range(i + 1, len(freq)):
                if freq[i][1] < freq[j][1]:
                    freq[i], freq[j] = freq[j], freq[i]
        return freq

    def count_freq(s):
        freq = []
        for _ in range(26):
            freq.append([chr(ord('a') + _), 0])
        for c in s:
            if is_alpha(c):
                freq[ord(to_lower(c)) - ord('a')][1] += 1
        return sort_freq(freq)

    for c in s:
        if not is_alpha(c):
            return False, "The string contains non-alphabetical characters."
    freq = count_freq(s)
    return True, [(c, f) for c, f in freq if f != 0]