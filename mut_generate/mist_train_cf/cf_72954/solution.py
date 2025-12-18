"""
QUESTION:
Implement a function named `are_anagrams` that determines whether two provided strings are anagrams of each other without utilizing any built-in library functions, data structures, or helper methods. The solution should not rely on any sorting algorithms and should have a time complexity better than O(n log n). The function should handle edge cases such as strings containing numbers, symbols, and spaces. The input to the function will be two strings, and the output should be a boolean value indicating whether the strings are anagrams or not.
"""

def are_anagrams(str1, str2):
    # Create two count arrays and initialize all values as 0
    count1 = [0] * 256
    count2 = [0] * 256

    # Iterate through every character of both strings
    for i in range(len(str1)):
        count1[ord(str1[i])] += 1
    for i in range(len(str2)):
        count2[ord(str2[i])] += 1

    # If both strings are of different length.
    # Removing this condition will make the program 
    # fail for strings like "aaca" and "aca"
    if len(str1) != len(str2):
        return False

    # Compare count arrays
    for i in range(256):
        if count1[i] != count2[i]:
            return False
        
    return True