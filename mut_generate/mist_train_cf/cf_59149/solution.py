"""
QUESTION:
Create a function named `advanced_histogram` that takes a string `test` as input and returns an object containing characters and their frequencies that have the highest frequency in the input string, ignoring spaces and considering only lowercase characters.
"""

def advanced_histogram(test):
    """Returns a dictionary containing characters and their frequencies 
    that have the highest frequency in the input string, ignoring spaces 
    and considering only lowercase characters."""
    
    count = {}
    for char in test:
        if char != ' ':
            char = char.lower()
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    max_freq = max(count.values()) if count else 0
    max_freq_chars = {key: value for key, value in count.items() if value == max_freq}

    return max_freq_chars