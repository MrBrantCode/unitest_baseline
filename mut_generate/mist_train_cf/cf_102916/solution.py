"""
QUESTION:
Create a function called `create_sorted_dict` that takes a string as input and returns a dictionary where the keys are the alphabetical letters in the string (case-sensitive) and the values are the frequency of each letter. The function should ignore non-alphabetical characters and the keys in the resulting dictionary should be sorted in alphabetical order.
"""

def create_sorted_dict(input_string):
    my_dict = {}
    
    for char in input_string:
        if char.isalpha():
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
                
    return dict(sorted(my_dict.items()))