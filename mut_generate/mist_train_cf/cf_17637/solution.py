"""
QUESTION:
Write a function `character_frequency(string)` that calculates the frequency of each alphabet character in a given string, ignoring case sensitivity. The function should have a time complexity of O(n) and a space complexity of O(1), excluding the space required for the output, where n is the length of the input string. The function should return a list of tuples containing characters and their frequencies in descending order of frequency.
"""

def character_frequency(string):
    frequency = [0] * 26
    for char in string:
        if char.isalpha():
            char = char.lower()
            frequency[ord(char) - ord('a')] += 1

    result = []
    for i in range(26):
        if frequency[i] > 0:
            char = chr(i + ord('a'))
            result.append((char, frequency[i]))

    result.sort(key=lambda x: x[1], reverse=True)
    return result