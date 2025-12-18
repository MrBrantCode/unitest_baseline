"""
QUESTION:
Implement the `advanced_histogram` function to process a string of mixed characters (uppercase and lowercase alphabets, numbers, and punctuation marks) separated by spaces. The function should return a dictionary containing the most frequently appearing characters (in lowercase format) and their counts. If multiple characters have the same highest count, include all of them in the dictionary.
"""

def advanced_histogram(test):
    # Track counts
    count = {}
    for char in test:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1

    # Find maximum count
    max_count = 0
    for char, cnt in count.items():
        if cnt > max_count:
            max_count = cnt
    
    # Collect chars that have max_count 
    max_chars = {}
    for char, cnt in count.items():
        if cnt == max_count:
            max_chars[char] = cnt
    
    return max_chars