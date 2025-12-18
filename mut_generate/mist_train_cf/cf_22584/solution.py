"""
QUESTION:
Write a function `find_needle(haystack, needle)` that finds the starting index of all occurrences of the needle within the haystack, considering both case sensitivity and partial matches, and returns the indices as a list in ascending order.

The haystack and needle are strings containing only alphabetic characters and spaces, with lengths not exceeding 10^5. Do not use any built-in functions or libraries that directly solve this problem.
"""

def find_needle(haystack, needle):
    haystack_lower = haystack.lower()
    needle_lower = needle.lower()
    words = haystack.split()
    indices = []
    
    for i, word in enumerate(words):
        if needle_lower in word.lower():
            index = word.lower().index(needle_lower)
            haystack_index = sum(len(words[j]) + 1 for j in range(i)) + index
            indices.append(haystack_index)
    
    return indices