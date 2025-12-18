"""
QUESTION:
Create a function named `find_strings` that takes an array of strings as input and returns a new array containing only the strings that start with the letter "a" and end with a consonant, along with the total number of matched strings.
"""

def find_strings(start_arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    end_arr = []
    for word in start_arr:
        if word[0].lower() == 'a' and word[-1].lower() not in vowels:
            end_arr.append(word)
    return end_arr, len(end_arr)