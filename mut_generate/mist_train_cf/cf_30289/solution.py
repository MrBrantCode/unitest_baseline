"""
QUESTION:
Implement the function `rearrangeString(freq)` that takes a list of integers `freq` representing the frequency of characters in a string, and returns a string representing the rearranged characters such that no two adjacent characters are the same. If it is not possible to rearrange the characters, return an empty string.

The input `freq` is a list of integers with a length in the range [1, 26], where each element is in the range [0, 100].
"""

def rearrangeString(freq):
    max_freq = max(freq)
    max_freq_char = chr(freq.index(max_freq) + ord('a'))
    freq[freq.index(max_freq)] -= 1
    result = max_freq_char

    while sum(freq) > 0:
        prev_char = result[-1]
        max_freq = max(freq)
        max_freq_char = chr(freq.index(max_freq) + ord('a'))
        if max_freq_char == prev_char:
            for i in range(26):
                if chr(i + ord('a')) != prev_char and freq[i] > 0:
                    max_freq_char = chr(i + ord('a'))
                    break
        freq[freq.index(max_freq)] -= 1
        result += max_freq_char

    return result if len(result) == sum(freq) + 1 else ""