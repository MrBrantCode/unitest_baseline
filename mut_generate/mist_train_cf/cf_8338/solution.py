"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns a boolean value. The function should perform a case-insensitive comparison of the input strings and check if they are anagrams of each other. The comparison should be implemented in a way that achieves a time complexity of O(n), where n is the length of the input strings, and a space complexity of O(1).
"""

def compare_strings(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()

    frequency = [0] * 26  # Assuming only lowercase alphabets

    for i in range(len(str1)):
        frequency[ord(str1[i]) - ord('a')] += 1
        frequency[ord(str2[i]) - ord('a')] -= 1

    return str1 == str2 and all(count == 0 for count in frequency)