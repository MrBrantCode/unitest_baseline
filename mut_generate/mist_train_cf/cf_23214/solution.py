"""
QUESTION:
Write a function `reverse_string` that takes a string as input, reverses the non-space characters without using any built-in string manipulation functions, and returns the reversed string. The function should also print the characters in the reversed string along with their frequencies in descending order. The input string can contain any characters, including spaces, and the function should ignore any spaces when reversing the string and calculating the character frequencies.
"""

def reverse_string(s):
    reversed_string = ''
    frequencies = {}

    # Reverse the non-space characters
    for char in s:
        if char != ' ':
            reversed_string = char + reversed_string

    # Count the frequency of each character in the reversed string
    for char in reversed_string:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    # Sort the characters based on their frequencies in descending order
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    # Print the characters along with their frequencies
    for char, frequency in sorted_frequencies:
        print(f"{char}: {frequency}")

    return reversed_string