"""
QUESTION:
Create a function called create_sorted_dict() that takes a string as input and returns a dictionary containing the sorted key-value pairs of letters from the input string. 

The function should ignore any non-alphabet characters and handle cases where the input string is empty or consists only of special characters or numbers. If a letter appears multiple times in the input string, its value in the dictionary should be the frequency of its occurrence. 

The function should return an empty dictionary if the input string is empty or does not contain any letters. The input string should have at least 5 characters and at most 100 characters.
"""

def create_sorted_dict(input_string):
    my_dict = {}
    
    for char in input_string:
        if char.isalpha():
            my_dict[char] = my_dict.get(char, 0) + 1
    
    return dict(sorted(my_dict.items()))