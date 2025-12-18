"""
QUESTION:
Create a function called `find_longest_word` that takes a JSON string as input and returns the longest word found inside, excluding any words that contain numbers, along with the count of occurrences of each character in the word. If there are multiple longest words with the same length, select the first longest word encountered. The JSON string may contain special characters, such as punctuation marks and spaces, which should be included in the word length and character occurrence counts.
"""

import json

def find_longest_word(json_string):
    # Parse the JSON string
    json_data = json.loads(json_string)
    
    longest_word = ""
    for key in json_data:
        # Extract the words as separate strings
        word = key
        
        # Exclude words that contain numbers
        if any(char.isdigit() for char in word):
            continue
        
        # Find the longest word
        if len(word) > len(longest_word):
            longest_word = word
    
    # Count the occurrences of each character in the longest word
    char_counts = {}
    for char in longest_word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return longest_word, char_counts