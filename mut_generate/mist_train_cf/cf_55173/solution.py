"""
QUESTION:
Categorize and sort an array of strings based on the number of vowels they contain. If strings have the same number of vowels, they should be sorted by their lengths. Return a dictionary where the keys are the count of vowels and the values are the sorted strings corresponding to that vowel count.

Write a function `categorize_and_sort` that takes an array of strings as input and returns the described dictionary. Assume the input array contains only strings and the vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase). The function should handle arrays of any length and strings of any length.
"""

def categorize_and_sort(arr):
    vowel_dict = {}
    for word in arr:
        vowel_count = sum(word.lower().count(c) for c in 'aeiou')
        if vowel_count not in vowel_dict:
            vowel_dict[vowel_count] = [word]
        else:
            vowel_dict[vowel_count].append(word)
    for key in vowel_dict:
        vowel_dict[key] = sorted(vowel_dict[key], key=len)
    
    return vowel_dict