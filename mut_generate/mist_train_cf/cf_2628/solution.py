"""
QUESTION:
Write a function `most_frequent_letter(s)` that finds the most frequent letter in a given string `s` and returns it. If there are multiple letters with the same highest frequency, return the letter that appears first in the string. If the string is empty or contains non-alphabetic characters, return an empty string. The function must have a time complexity of O(n), where n is the length of the string, and cannot use external libraries or built-in functions for string manipulation or counting. The string `s` can have a maximum length of 10^5 characters.
"""

def most_frequent_letter(s):
    count = [0] * 26
    maxCount = 0
    mostFrequent = ""

    for c in s:
        if not c.isalpha():
            return ""
        c = c.lower()
        index = ord(c) - ord('a')
        count[index] += 1

        if count[index] > maxCount:
            maxCount = count[index]
            mostFrequent = c
        elif count[index] == maxCount and s.find(c) < s.find(mostFrequent):
            mostFrequent = c

    return mostFrequent