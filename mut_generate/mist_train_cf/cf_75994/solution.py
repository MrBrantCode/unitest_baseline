"""
QUESTION:
Create a function `find_occurrences(s1, s2)` that accepts two strings `s1` and `s2` as input and finds all occurrences of `s1` as a substring of `s2` without using built-in substring functions. The function should return the start and end indices of each occurrence. If no occurrence is found, it should display an appropriate message. The function should handle cases that involve non-alphanumeric characters and/or spaces and all possible edge cases and errors gracefully.
"""

def find_occurrences(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    occurrences = []

    if len_s1 > len_s2:
        print("First string cannot be a substring of the second.")
        return

    for i in range(len_s2 - len_s1 + 1):
        match = True
        for j in range(len_s1):
            if s1[j] != s2[i+j]:
                match = False
                break
        if match:
            occurrences.append((i, i+len_s1-1))

    if not occurrences:
        print("Substring not found.")
    else:
        print("Substring found at:")
        for start, end in occurrences:
            print(f"Start index: {start}, End index: {end}")