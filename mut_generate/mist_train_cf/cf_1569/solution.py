"""
QUESTION:
Write a function named `get_second_to_last` that takes an array of strings as input. If the array contains less than 5 elements, return an empty string. Otherwise, check the second to last element of the array; if its length is 7 characters or less, return an empty string. Among all elements in the array with more than 7 characters, find the one with the most consonants and return it. If no such element exists, return -1.
"""

def get_second_to_last(arr):
    if len(arr) < 5:
        return ""
    
    second_to_last = arr[-2]
    
    if len(second_to_last) <= 7:
        return ""
    
    max_consonants = 0
    result = ""
    
    for string in arr:
        if len(string) > 7:
            consonants = sum(1 for char in string.lower() if char not in "aeiou")
            if consonants > max_consonants:
                max_consonants = consonants
                result = string
    
    return result if result != "" else -1