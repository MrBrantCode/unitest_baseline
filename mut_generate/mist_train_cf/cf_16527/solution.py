"""
QUESTION:
Write a function `retrieve_second_to_last(arr)` that retrieves the second to last element of a given array of strings if it has at least 3 elements and the second to last element is longer than 5 characters. If there are multiple strings in the array that meet the criteria, the function should return the string with the highest number of vowels. If the array has less than 3 elements or the second to last element is shorter or equal to 5 characters, the function should return an empty string. If there are no strings that meet the criteria, the function should return -1.
"""

def retrieve_second_to_last(arr):
    if len(arr) < 3:
        return ""
    
    second_to_last = arr[-2]
    if len(second_to_last) <= 5:
        return ""
    
    longest_string = ""
    highest_vowel_count = 0
    
    for string in arr:
        if len(string) > 5 and string != second_to_last:
            vowel_count = 0
            for char in string:
                if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                    vowel_count += 1
            if vowel_count > highest_vowel_count:
                longest_string = string
                highest_vowel_count = vowel_count
    
    if longest_string != "":
        return longest_string
    
    return -1