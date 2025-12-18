"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks if two given strings `s1` and `s2` are anagrams of each other. The function should not use built-in library functions or data structures and must check that the two strings do not contain any non-alphabetic symbols. If the strings are anagrams, the function should print a message confirming this. If not, it should print a message indicating that the strings are not anagrams. Additionally, the function should count and print out every character's frequency in both strings.
"""

def are_anagrams(s1, s2):
    # Check for non-alphabetic symbols
    for c in s1+s2:
        if not c.isalpha():
            print("Non-alphabetic symbol found!")
            return False

    # Ascii values for small alphabets starts from 97 and ends at 122.
    # So we just need an array of size 26 for case in-sensitive comparison.
    count = [0] * 26

    # Count frequency for string s1
    for i in range(len(s1)):
        count[ord(s1[i].lower()) - 97] += 1

    # Subtract frequency for string s2
    for i in range(len(s2)):
        count[ord(s2[i].lower()) - 97] -= 1
  
    # If the two strings are anagrams,
    # the count array should be back to all zeros.
    for i in range(26):
        if count[i] != 0:
            print("Strings are not anagrams of each other.")
            return False

    # If no error has occurred, they are anagrams.
    print("Strings are anagrams of each other.")
    return True