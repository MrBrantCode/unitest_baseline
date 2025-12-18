"""
QUESTION:
Write a function named `find_most_frequent_char` that finds the most frequent character in a given string, considering both uppercase and lowercase characters. The function must have a time complexity of O(n), where n is the length of the input string, and cannot use any additional data structures such as arrays, dictionaries, or sets. The input string will have a maximum length of 1,000,000 characters.
"""

def find_most_frequent_char(input_string):
    most_frequent_char = input_string[0]
    max_frequency = 1
    current_char = input_string[0]
    current_frequency = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            current_frequency += 1
        else:
            if current_frequency > max_frequency:
                max_frequency = current_frequency
                most_frequent_char = current_char
            current_char = input_string[i]
            current_frequency = 1

    if current_frequency > max_frequency:
        max_frequency = current_frequency
        most_frequent_char = current_char

    return most_frequent_char