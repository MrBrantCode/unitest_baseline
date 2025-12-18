"""
QUESTION:
Create a function called `count_characters` that takes a string and an optional threshold value (defaulting to 1) as input. The function should return a dictionary where the keys are unique alphabetical characters from the string (case-insensitive) and the values are their corresponding counts, sorted in descending order by count. Exclude any characters with a count less than or equal to the threshold value.
"""

def count_characters(string, threshold=1):
    char_counts = {}
    
    for char in string:
        if char.isalpha():
            char = char.lower()
            
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    filtered_counts = {char: count for char, count in sorted_counts if count > threshold}
    
    return filtered_counts