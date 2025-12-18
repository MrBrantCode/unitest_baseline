"""
QUESTION:
Create a function called `analyze_a_occurrences` that takes a string as input and returns a tuple containing the total count of the letter "a" (both uppercase and lowercase), the 1-based index of the first occurrence of "a", and the 1-based index of the last occurrence of "a". If "a" does not occur in the string, the function should return the corresponding indices as -1 or any other appropriate value.
"""

def analyze_a_occurrences(input_string):
    # Convert the input string to lowercase to count both uppercase and lowercase occurrences of 'a'
    lowercase_string = input_string.lower()
    
    # Calculate the total count of the letter 'a'
    total_count = lowercase_string.count('a')
    
    # Determine the position of the first occurrence of the letter 'a'
    first_position = lowercase_string.find('a') + 1 if lowercase_string.find('a') != -1 else -1
    
    # Find the position of the last occurrence of the letter 'a'
    last_position = lowercase_string.rfind('a') + 1 if lowercase_string.rfind('a') != -1 else -1
    
    return total_count, first_position, last_position