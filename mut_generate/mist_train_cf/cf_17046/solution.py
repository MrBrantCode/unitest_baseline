"""
QUESTION:
Create a function called create_sorted_dict() that takes a string as input and returns a dictionary. The function should count the occurrences of each letter in the string, ignoring non-alphabet characters, and return the counts in a dictionary with keys sorted in alphabetical order.
"""

def create_sorted_dict(input_string):
    my_dict = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return dict(sorted(my_dict.items()))