"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that checks if two input strings are anagrams of each other. The function should ignore special characters, be case-insensitive, have a time complexity of O(n), and a space complexity of O(1), where n is the total number of characters in both strings.
"""

def are_anagrams(str1, str2):
    # Step 1: Removing special characters and converting to lowercase
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # Step 2: Initializing frequency counter array
    freq_counter = [0] * 26

    # Step 3: Incrementing frequency counter for str1
    for char in str1:
        index = ord(char) - ord('a')
        freq_counter[index] += 1

    # Step 4: Decrementing frequency counter for str2
    for char in str2:
        index = ord(char) - ord('a')
        freq_counter[index] -= 1

    # Step 5: Checking if all frequencies are zero
    for count in freq_counter:
        if count != 0:
            return False

    return True