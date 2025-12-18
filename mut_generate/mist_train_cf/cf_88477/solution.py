"""
QUESTION:
Write a function called `are_anagrams` that takes two strings as input and returns a boolean indicating whether they are anagrams of each other. The function should have a time complexity of O(n), where n is the length of the input strings, and should not use any built-in functions or libraries for sorting or counting characters. Additionally, the function should not use any additional data structures such as dictionaries, lists, or sets to solve this problem, except for a single list of fixed size. Assume the input strings contain only lowercase letters.
"""

def are_anagrams(str1, str2):
    if len(str1) != len(str2):  # Anagrams must have same length
        return False

    char_counts = [0] * 26  # Assuming the strings contain only lowercase letters

    for i in range(len(str1)):
        char_counts[ord(str1[i]) - ord('a')] += 1
        char_counts[ord(str2[i]) - ord('a')] -= 1

    for count in char_counts:
        if count != 0:  # If any character count is non-zero, they are not anagrams
            return False

    return True