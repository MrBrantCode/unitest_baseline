"""
QUESTION:
Write a function `sort_strings` that sorts a list of strings in alphabetical order, ignoring the case of the letters, and preserving duplicates. The function should not use any additional memory space other than the input list and should have a time complexity of O(n^2).
"""

def sort_strings(strings):
    n = len(strings)
    
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Ignore case of letters while comparing strings
            if strings[j].lower() > strings[j+1].lower():
                # Swap strings if they are in wrong order
                strings[j], strings[j+1] = strings[j+1], strings[j]
    
    return strings