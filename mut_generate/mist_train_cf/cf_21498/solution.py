"""
QUESTION:
Write a function `remove_common_letters` that takes two strings as input and returns a list of tuples, where each tuple contains a unique letter that is present in only one of the strings, and its frequency. The list should be sorted in descending order based on the frequency of the letters. The function should have a time complexity of O(n), where n is the length of the strings, and should not use any built-in functions or libraries for sorting or character manipulation.
"""

def remove_common_letters(string1, string2):
    # Create dictionaries to store the frequency of letters in each string
    freq1 = [0] * 256
    freq2 = [0] * 256

    # Count the frequency of letters in string1
    for char in string1:
        freq1[ord(char)] += 1

    # Count the frequency of letters in string2
    for char in string2:
        freq2[ord(char)] += 1

    # Remove common letters and update their frequencies
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

    # Sort the removed letters in lexicographical order
    removed_letters.sort()

    # Create a dictionary to store the frequency of each removed letter
    removed_freq = {}
    for char in removed_letters:
        if char in removed_freq:
            removed_freq[char] += 1
        else:
            removed_freq[char] = 1

    # Sort the removed letters by their frequencies in descending order
    sorted_removed = sorted(removed_freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_removed