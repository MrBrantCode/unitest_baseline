"""
QUESTION:
Write a function named `search_string` that takes two parameters: an array of strings `arr` and a string `given_str`. The function should search for `given_str` within the array, considering only strings that start with a capital letter, contain at least one vowel, and have a length of at least 5 characters. The search should be case-sensitive. The function should return the index of the first occurrence of `given_str` in the filtered array. If `given_str` is not found, the function should return -1.
"""

def search_string(arr, given_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_arr = [string for string in arr if string[0].isupper() and any(vowel in string.lower() for vowel in vowels) and len(string) >= 5]
    try:
        return filtered_arr.index(given_str)
    except ValueError:
        return -1