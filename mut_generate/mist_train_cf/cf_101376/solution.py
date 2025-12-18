"""
QUESTION:
Create a Python function `sort_fruits_by_cumulative_vowels` that takes a list of strings representing fruit names as input and returns a new list where the fruit names are arranged in order of increasing cumulative vowel count. The function should handle error cases where the input list is empty or contains non-string elements, returning an empty list in such cases.
"""

def sort_fruits_by_cumulative_vowels(fruit_list):
    # Check if input is empty or contains non-string elements
    if not fruit_list:
        return []
    for fruit in fruit_list:
        if not isinstance(fruit, str):
            return []
    
    # Define a function to calculate cumulative vowel count in a string
    def cumulative_vowel_count(string):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in string:
            if char in vowels:
                count += 1
        return count
    
    # Sort the list of fruits based on cumulative vowel count
    sorted_fruits = sorted(fruit_list, key=cumulative_vowel_count)
    
    return sorted_fruits