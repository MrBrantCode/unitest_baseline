"""
QUESTION:
Create a function `modify_strings` that takes a list of strings as input and returns a new list of strings. The function should only include strings with an uppercase first letter and no vowels, reverse each string, and sort the list in alphabetical order. The time complexity of the solution should be O(nlogn) and the space complexity should be O(n), where n is the length of the input list.
"""

def modify_strings(input_list):
    result = []

    for string in input_list:
        if string[0].isupper() and all(letter.lower() not in 'aeiou' for letter in string):
            result.append(string[::-1])

    result.sort()
    return result