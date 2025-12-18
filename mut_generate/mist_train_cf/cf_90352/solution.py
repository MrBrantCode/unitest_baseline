"""
QUESTION:
Implement a function called `compare_strings` that takes two strings `str1` and `str2` as input, and returns `True` if the strings are equal in a case-insensitive manner and are anagrams of each other, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the input strings, and a space complexity of O(1).
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