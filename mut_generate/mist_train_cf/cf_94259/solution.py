"""
QUESTION:
Write a function named `print_consecutive_chars` that takes a string as input. The function should print the input string and the count of consecutive identical characters if the string contains five or more consecutive identical characters (excluding spaces) and the string is at least 10 characters long. If no such consecutive characters are found, print a message indicating so.
"""

def print_consecutive_chars(input_string):
    if len(input_string) < 10:
        print("String is less than 10 characters")
        return

    consecutive_count = 0
    prev_char = None

    for char in input_string:
        if char == prev_char and char != ' ':
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        if consecutive_count >= 5:
            print(input_string)
            print("Consecutive count:", consecutive_count)
            break

        prev_char = char

    else:
        print("No consecutive characters found")