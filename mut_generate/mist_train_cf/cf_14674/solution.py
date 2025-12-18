"""
QUESTION:
Write a function named `count_letters` that takes a string as input, counts the occurrences of each unique letter in the string while ignoring case sensitivity and non-alphabetical characters, and returns the counts in descending order. The function should return a list of tuples, where each tuple contains a letter and its corresponding count.
"""

def count_letters(string):
    counts = {}
    string = string.lower()
    
    for char in string:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts