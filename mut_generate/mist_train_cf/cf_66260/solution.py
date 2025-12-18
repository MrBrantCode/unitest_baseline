"""
QUESTION:
Write a function called `are_anagrams` that takes two lists of strings as input. The function must determine whether each string pair across the lists are anagrams of each other. The function should handle variation in letter case and ignore punctuation and spaces. The function should return True if all string pairs are anagrams, and False otherwise.
"""

def are_anagrams(list1, list2):
    def sanitize_string(s):
        s = s.replace(" ", "")
        s = ''.join(e for e in s if e.isalnum())
        s = s.lower()
        return s

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        s1 = sanitize_string(list1[i])
        s2 = sanitize_string(list2[i])

        if sorted(s1) != sorted(s2):
            return False
            
    return True