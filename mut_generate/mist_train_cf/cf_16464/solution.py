"""
QUESTION:
Write a function `print_consecutive_chars` that takes a string as input and prints the string along with the count of consecutive identical characters if the string contains at least five consecutive identical characters and is at least 10 characters long. The function should ignore any consecutive characters that are followed by a space character.
"""

def print_consecutive_chars(string):
    if len(string) < 10:
        return

    consecutive_count = 0
    prev_char = None

    for char in string:
        if char == prev_char and char != ' ':
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        if consecutive_count >= 5:
            print(string)
            print("Consecutive count:", consecutive_count)
            break

        prev_char = char

    else:
        return