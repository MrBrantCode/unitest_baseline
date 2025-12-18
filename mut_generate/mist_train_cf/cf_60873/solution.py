"""
QUESTION:
Write a function `advanced_histogram` that takes a string composed of space-separated characters (including uppercase and lowercase alphabets, digits, and punctuation marks) as input. The function should output a dictionary detailing the character(s) with the maximum frequency (in lowercase for alphabets) alongside the corresponding count. If there are multiple characters sharing the same frequency, return them all. The function should treat uppercase and lowercase letters as not distinct.
"""

def advanced_histogram(test):
    count = {}
    for char in test:
        if char != ' ':
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    # Finding the maximum frequency
    max_freq = max(count.values()) if count else 0

    # Using a dictionary comprehension to filter the results
    max_freq_chars = {k: v for k, v in count.items() if v == max_freq}

    return max_freq_chars