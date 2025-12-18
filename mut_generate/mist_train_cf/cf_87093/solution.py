"""
QUESTION:
Write a function named `compare_strings` that compares two input strings character by character and returns the number of differing characters and their positions. The function should consider uppercase and lowercase characters as different, handle strings of different lengths by counting extra characters in the longer string as differing characters, and include special and Unicode characters in the comparison. It should also count each occurrence of a differing character separately. The function should aim for an efficient solution with optimal time and space complexity.
"""

def compare_strings(string_a, string_b):
    diff_count = 0
    diff_positions = []
    
    len_a = len(string_a)
    len_b = len(string_b)
    max_len = max(len_a, len_b)
    
    for i in range(max_len):
        if i >= len_a or i >= len_b or string_a[i] != string_b[i]:
            diff_count += 1
            diff_positions.append(i)
    
    return diff_count, diff_positions