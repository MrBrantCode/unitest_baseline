"""
QUESTION:
Write a function called `are_anagrams` that takes two strings as input and determines if they are anagrams of each other. The function must have a time complexity of O(n log n), use constant space, and cannot use built-in sorting or hashing functions. The function should also handle uppercase and lowercase letters as equivalent.
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