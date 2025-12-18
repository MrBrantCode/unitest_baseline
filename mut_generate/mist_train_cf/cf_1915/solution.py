"""
QUESTION:
Implement a function called `is_anagram(s1, s2)` that determines whether `s1` is an anagram of `s2`. The function should convert both strings to lowercase, remove non-alphabetic characters, sort the characters in each string, and compare the sorted strings. The function should return `True` if `s1` is an anagram of `s2` and `False` otherwise.

The solution must satisfy the following constraints: 

- Space complexity of O(1), meaning no additional data structures other than the input strings and a constant amount of extra space.
- Ability to handle strings with a maximum length of 10^6 characters.
- Ability to handle anagrams of strings formed by rearranging the letters of the alphabet, including both uppercase and lowercase letters.
- No use of built-in functions or libraries for sorting or comparing strings.
- Time complexity that allows the solution to run within a time limit of 2 seconds for any given input.
"""

def is_anagram(s1, s2):
    # Step 1: Convert both s1 and s2 to lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Step 2: Remove any non-alphabetic characters
    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())

    # Step 3: Sort the characters in s1 and s2
    s1 = sort_string(s1)
    s2 = sort_string(s2)

    # Step 4: Compare the sorted strings
    if s1 == s2:
        return True
    else:
        return False

# Helper function to sort the characters in a string
def sort_string(s):
    n = len(s)
    s = list(s)
    
    # Implementing insertion sort
    for i in range(1, n):
        key = s[i]
        j = i-1
        while j >= 0 and s[j] > key:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = key

    return ''.join(s)