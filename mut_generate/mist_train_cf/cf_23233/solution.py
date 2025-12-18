"""
QUESTION:
Write a function `count_vowels(strings)` that takes a list of strings as input. The function should count the number of occurrences of each string that contains at least one vowel and starts with a lowercase letter. Return a dictionary where the keys are the strings that meet these conditions and the values are their respective counts. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def count_vowels(strings):
    count_dict = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for string in strings:
        if not string[0].isupper():
            if any(vowel in string.lower() for vowel in vowels):
                if string in count_dict:
                    count_dict[string] += 1
                else:
                    count_dict[string] = 1
    
    return count_dict