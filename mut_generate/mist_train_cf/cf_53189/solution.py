"""
QUESTION:
Implement the function `advanced_histogram` that takes a string of space-separated characters (including uppercase and lowercase letters, numbers, and punctuation) and returns a dictionary representing the most frequent characters (in lowercase for letters) along with their count. In cases where multiple characters share the same count, include all of them in the return dictionary. The function should treat uppercase and lowercase letters as identical.
"""

def advanced_histogram(test):
    count = {}
    max_count = 0
    max_count_chars = []
    
    # Counting frequency of all characters
    for char in test:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
            # Keeping track of maximum count
            if count[char.lower()] > max_count:
                max_count = count[char.lower()]

    # Adding characters with max_count in list
    for char, char_count in count.items():
        if char_count == max_count:
            max_count_chars.append(char)

    # Preparing final dictionary
    result = {char: max_count for char in max_count_chars}
    return result