"""
QUESTION:
Write a function named `longest_uppercase_run` that takes a string as input and returns the length of the longest run of consecutive uppercase letters. The function must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), without using any additional data structures.
"""

def longest_uppercase_run(string):
    max_run = 0
    current_run = 0

    for i in range(len(string)):
        if string[i].isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run