"""
QUESTION:
Create a function named `sort_strings` that sorts an array of strings in ascending order. The sorting criteria are as follows: 
- First, by the number of vowels in a string 
- Then, by the length of the string 
- Finally, alphabetically if the above criteria are equal. 

The function should not use the built-in sort() function.
"""

VOWELS = ('a', 'e', 'i', 'o', 'u')

def count_vowels(string):
    return sum(1 for char in string if char.lower() in VOWELS)

def sort_strings(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            vowel_count_first_string = count_vowels(arr[j])
            vowel_count_second_string = count_vowels(arr[j + 1])
            if (vowel_count_first_string > vowel_count_second_string) or (
               vowel_count_first_string == vowel_count_second_string and
               len(arr[j]) > len(arr[j + 1])) or (
               vowel_count_first_string == vowel_count_second_string and
               len(arr[j]) == len(arr[j + 1]) and
               arr[j].lower() > arr[j + 1].lower()
            ):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr