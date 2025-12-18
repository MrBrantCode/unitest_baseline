"""
QUESTION:
Write a program that takes a string input from the user, reverses the string, removes any duplicate characters, and counts the frequency of each character in the original string. The program should print the reversed string, the string without duplicates, and the character frequencies in descending order. The input string can contain lowercase alphabets and spaces.
"""

def entrance(string):
    reversed_string = string[::-1]
    unique_chars = []
    for char in reversed_string:
        if char not in unique_chars:
            unique_chars.append(char)
    unique_string = ''.join(unique_chars)
    
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    return reversed_string, unique_string, sorted_frequency