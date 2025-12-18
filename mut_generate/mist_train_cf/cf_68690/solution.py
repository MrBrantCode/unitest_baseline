"""
QUESTION:
Design a function `elaborate_histogram(test)` that takes a string of space-separated characters, processes them in a case-insensitive manner (treating uppercase and lowercase letters as equivalent), and returns a dictionary containing the most frequent character(s) in lowercase for letters and their count. If there are multiple characters with the same highest frequency, include all of them in the dictionary.
"""

def elaborate_histogram(test):
    count = {}
    for char in test:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
                
    max_count = max(count.values(), default=0)
    return {char: count_ for char, count_ in count.items() if count_ == max_count}