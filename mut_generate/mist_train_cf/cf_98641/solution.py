"""
QUESTION:
Write a function `count_unique_characters` that takes a string input and returns the count of unique characters present in it. The input string should have at least 10 non-space characters and may contain uppercase characters, duplicate letters, and whitespace. The function should preprocess the input by removing whitespace and converting to lowercase, count unique characters using a set, and post-process the result by printing a table of input strings and their corresponding unique character counts.
"""

def count_unique_characters(string):
    # Preprocessing the input string
    string = string.replace(" ", "").lower()
    
    # Counting the unique characters
    unique_chars = set(string)
    unique_count = len(unique_chars)
    
    # Post-processing the result
    print("| Input String | Unique Character Count |")
    print("|--------------|-----------------------|")
    print(f"| {string} | {unique_count} |")
    
    return unique_count