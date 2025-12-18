"""
QUESTION:
Create a function `count_vowels(strings)` that takes a list of strings as input and returns a dictionary where each string from the list is a key and its corresponding value is the number of vowels in the string. The dictionary should be sorted by the number of vowels in descending order, and for strings with the same number of vowels, they should be sorted alphabetically. The function should have a time complexity of O(nlogn) and a space complexity of O(n), where n is the length of the input list.
"""

def count_vowels(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = {}
    for string in strings:
        count = 0
        for char in string:
            if char.lower() in vowels:
                count += 1
        counts[string] = count
    
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return dict(sorted_counts)