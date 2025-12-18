"""
QUESTION:
Write a function `move_numbers_to_end_and_count` that takes a string as input, moves all numbers to the end of the string while maintaining the relative order of non-numeric characters, and returns a tuple containing the count of unique numbers found in the string and the modified string. The function should not alter the relative order of the non-numeric characters and should consider each digit as a separate number.
"""

def move_numbers_to_end_and_count(input_str):
    numbers = []
    other_chars = []
    unique_numbers = set()
    
    for char in input_str:
        if char.isdigit():
            numbers.append(char)
            unique_numbers.add(char)
        else:
            other_chars.append(char)
    
    result_str = ''.join(other_chars + numbers)
    
    return len(unique_numbers), result_str