"""
QUESTION:
Write a function `count_character_frequency(input_string)` that calculates the frequency of alphabets in a given input string, ignoring non-alphabet characters and considering 'a' and 'A' as the same character. The function should return a dictionary with unique alphabets as keys and their frequencies as values. The time complexity should be O(n), where n is the length of the input string, and the space complexity should be O(1) or O(26). The function should not use any built-in functions or libraries for counting the frequency of characters.
"""

def count_character_frequency(input_string):
    frequency = [0] * 26  # Initialize frequency list with 26 zeros for each alphabet

    for char in input_string:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')  # Convert the character to lowercase and calculate the index
            frequency[index] += 1

    character_frequency = {}  # Initialize an empty dictionary for storing the character frequency

    for i in range(26):
        if frequency[i] > 0:
            character_frequency[chr(ord('a') + i)] = frequency[i]  # Convert the index back to character and store the frequency

    return character_frequency