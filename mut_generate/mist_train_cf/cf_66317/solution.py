"""
QUESTION:
Write a function `vowel_neighbor_counter` that takes a string as input and returns a dictionary where the keys are characters that have vowels as their neighbors in the string and the values are the counts of these characters. The function should handle both lower and upper case letters and treat them as the same. The function should ignore the first and last characters of the string.
"""

def vowel_neighbor_counter(string):
    vowels = "aeiouAEIOU"
    counter = {}
    for i in range(1,len(string)-1):
        if string[i-1] in vowels and string[i+1] in vowels:
            character = string[i].lower()
            if character not in counter:
                counter[character] = 1
            else:
                counter[character] += 1
    return counter