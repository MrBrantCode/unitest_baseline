"""
QUESTION:
Write a function called `filter_unique_strings` that takes a list of strings as input and returns a list of unique strings (excluding duplicates) that do not start with a vowel, sorted in descending order by length and then alphabetically. The function should be able to handle a list of up to 10^6 strings, each with a maximum length of 100 characters, and should have a time complexity of O(nlogn) or better.
"""

def filter_unique_strings(strings):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_counts = {}
    
    for string in strings:
        string_counts[string] = string_counts.get(string, 0) + 1
    
    unique_strings = []
    
    for string, count in string_counts.items():
        if count == 1 and not string.lower().startswith(tuple(vowels)):
            unique_strings.append(string)
    
    unique_strings.sort(key=lambda x: (-len(x), x))
    
    return unique_strings