"""
QUESTION:
Write a function `remove_common_letters` that takes two strings as input and returns a list of tuples, where each tuple contains a letter that is present in only one of the strings and its frequency. The list should be sorted in descending order based on the frequency of the letters. The function should have a time complexity of O(n), where n is the length of the strings, and should not use any built-in functions or libraries for sorting or character manipulation. The strings may contain any printable ASCII characters and have a maximum length of 10^5 characters.
"""

def remove_common_letters(string1, string2):
    freq1 = [0] * 256
    freq2 = [0] * 256

    for char in string1:
        freq1[ord(char)] += 1

    for char in string2:
        freq2[ord(char)] += 1

    removed_letters = []
    for char in string1:
        if freq2[ord(char)] == 0:
            removed_letters.append(char)
        else:
            freq2[ord(char)] -= 1

    for char in string2:
        if freq1[ord(char)] == 0:
            removed_letters.append(char)
        else:
            freq1[ord(char)] -= 1

    removed_letters.sort()

    removed_freq = {}
    for char in removed_letters:
        if char in removed_freq:
            removed_freq[char] += 1
        else:
            removed_freq[char] = 1

    sorted_removed = sorted(removed_freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_removed