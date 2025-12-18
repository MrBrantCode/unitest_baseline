"""
QUESTION:
Create a function `anagram_check(string1, string2)` that takes two character sequences of unequal magnitudes as input and returns `True` if they are anagrammatic counterparts of each other, considering case sensitivity. The function should bypass non-alphabetic symbols in the sequences. If the sequences are not anagrams, return `False` along with the positions of discrepancy between the character sequences.
"""

def anagram_check(string1, string2):
    str1 = [ch for ch in sorted(string1) if ch.isalpha()]
    str2 = [ch for ch in sorted(string2) if ch.isalpha()]

    # Check if strings are anagrams
    if str1 == str2:
        return True
    else:
        # If strings are not anagrams, indicate positions of discrepancy
        diff_positions = [i for i in range(min(len(str1), len(str2))) if str1[i] != str2[i]]

        # Append the remaining indices if strings are of different lengths
        if len(str1) != len(str2):
            diff_positions += list(range(min(len(str1), len(str2)), max(len(str1), len(str2))))

        return False, diff_positions