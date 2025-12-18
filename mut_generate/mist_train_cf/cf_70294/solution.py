"""
QUESTION:
Write a function `find_compact_subsequence` that takes a string `input_str` as input and returns the most compact subsequence that includes every unique alphabetic character in the input string, handling special characters and numbers. The function should be case sensitive, consider upper and lower case letters as distinct characters, and return the subsequence with a unique arrangement of characters, sorted in order of their appearance.
"""

def find_compact_subsequence(input_str):
    char_positions = {}
    for idx, char in enumerate(input_str):
        if char not in char_positions:
            char_positions[char] = [idx, idx]
        else:
            char_positions[char][1] = idx

    subsequences = sorted(char_positions.values(), key=lambda t: t[0])

    compact_subsequence = []
    current_subsequence = subsequences[0]
    for next_subsequence in subsequences[1:]:
        if next_subsequence[0] <= current_subsequence[1]:
            current_subsequence[1] = max(current_subsequence[1], next_subsequence[1])
        else:
            compact_subsequence.append(input_str[current_subsequence[0]:current_subsequence[1] + 1])
            current_subsequence = next_subsequence

    compact_subsequence.append(input_str[current_subsequence[0]:current_subsequence[1] + 1])

    return "".join(compact_subsequence)