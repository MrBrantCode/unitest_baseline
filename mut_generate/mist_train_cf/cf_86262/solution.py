"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that determines if two strings are anagrams of each other. The function should have a time complexity of O(n log n), where n is the length of the strings, and use constant space. The function should handle both uppercase and lowercase letters as equivalent and not use any built-in sorting or hashing functions to solve the problem.
"""

def are_anagrams(str1, str2):
    # Convert the strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if the lengths are different
    if len(str1) != len(str2):
        return False

    # Initialize the count arrays
    count1 = [0] * 26
    count2 = [0] * 26

    # Count the occurrences of each character in str1 and str2
    for i in range(len(str1)):
        count1[ord(str1[i]) - ord('a')] += 1
        count2[ord(str2[i]) - ord('a')] += 1

    # Compare the count arrays
    for i in range(26):
        if count1[i] != count2[i]:
            return False

    return True