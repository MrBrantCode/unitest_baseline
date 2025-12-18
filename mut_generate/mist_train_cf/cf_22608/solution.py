"""
QUESTION:
Create a function `compare_strings(str1, str2)` that compares two input strings and returns their equality status, the number of different characters, and the duplicate characters found in both strings along with their counts. The function should have a time complexity of O(n log n) or better, where n is the length of the longer string. The duplicate characters should be printed in alphabetical order, and the count of each duplicate character should be the minimum of its occurrences in the two strings.
"""

def compare_strings(str1, str2):
    if str1 == str2:
        return "Equal strings", 0, {}

    diff_count = 0
    diff_chars = set()
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            diff_count += 1
            diff_chars.add(char1)
            diff_chars.add(char2)
    
    diff_count += abs(len(str1) - len(str2))

    duplicate_chars = {char: min(str1.count(char), str2.count(char)) 
                       for char in set(str1) & set(str2) 
                       if min(str1.count(char), str2.count(char)) > 1}
    
    return "Unequal strings", diff_count, dict(sorted(duplicate_chars.items()))