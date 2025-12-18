"""
QUESTION:
Write a function `find_max_consecutive_vowels` that takes a string as input and returns the maximum number of consecutive vowels and the corresponding substring. The function should consider both lowercase and uppercase vowels. The string only contains alphabets.
"""

def find_max_consecutive_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_count = 0
    current_count = 0
    max_substring = ""
    current_substring = ""

    for char in string:
        if char.lower() in vowels:
            current_count += 1
            current_substring += char
        else:
            if current_count > max_count:
                max_count = current_count
                max_substring = current_substring
            current_count = 0
            current_substring = ""

    # Check if the last substring has more consecutive vowels than the previous maximum
    if current_count > max_count:
        max_count = current_count
        max_substring = current_substring

    return max_count, max_substring