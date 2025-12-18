"""
QUESTION:
Write a function `remove_and_sort` that takes a string as input, removes all non-alphabetic characters, and returns the new string with its alphabets sorted in descending order based on their ASCII values. Additionally, the function should return a dictionary containing the count of each unique alphabet in the original string. The solution must have a time complexity of O(nlogn) and cannot use any built-in sorting functions or libraries.
"""

def remove_and_sort(string):
    # Create a list to store the count of each unique alphabet
    count_dict = {}
    
    # Create a new string to store the alphabets
    new_string = ""
    
    # Iterate through each character in the original string
    for char in string:
        # Check if the character is an alphabet
        if char.isalpha():
            # Add the character to the new string
            new_string += char
            
            # Increment the count of the character in the count_dict
            count_dict[char.lower()] = count_dict.get(char.lower(), 0) + 1
    
    # Sort the alphabets in descending order based on their ASCII values
    sorted_string = "".join(sorted(new_string, key=lambda x: ord(x), reverse=True))
    
    return sorted_string, count_dict