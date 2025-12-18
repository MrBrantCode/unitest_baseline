"""
QUESTION:
Create a function named `sort_array` that takes an array of strings as input and returns the array sorted in ascending order first by string length and then by the number of vowels within strings of the same length, while maintaining the original order for strings with the same number of vowels and length.
"""

def sort_array(arr):
    def calculate_key(s):
        vowels = 'aeiou'
        return len(s), sum(c in vowels for c in s)

    return sorted(arr, key=calculate_key)