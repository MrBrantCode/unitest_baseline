"""
QUESTION:
Implement a function named `sort_strings` that takes a list of strings as input and returns the list sorted first by the length of the strings and then alphabetically within each length group, ignoring the case of the letters. The function must have a time complexity of O(n^2) and cannot use any additional memory space other than the input list.
"""

def sort_strings(strings):
    n = len(strings)

    for i in range(n):
        for j in range(0, n-i-1):
            # Compare strings based on length
            if len(strings[j]) > len(strings[j+1]):
                strings[j], strings[j+1] = strings[j+1], strings[j]
            # If lengths are equal, compare strings alphabetically (ignore case)
            elif len(strings[j]) == len(strings[j+1]) and strings[j].lower() > strings[j+1].lower():
                strings[j], strings[j+1] = strings[j+1], strings[j]
    
    return strings