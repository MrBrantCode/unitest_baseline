"""
QUESTION:
Implement a function `contains_hello` that takes a string as input and returns a boolean value indicating whether the string contains the word "hello" in any case, along with the count of occurrences of "hello". The function should have a time complexity of O(n), where n is the length of the string, and should be case-insensitive without using built-in string manipulation functions like `str.lower()` or `str.count()`. The function should handle overlapping occurrences of "hello".
"""

def contains_hello(string):
    # Convert the string and the word "hello" to lowercase using ASCII values
    string = ''.join(chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in string)
    word = "hello"

    # Initialize a count variable to keep track of the number of occurrences
    count = 0

    # Initialize a variable to keep track of the starting index of each occurrence
    index = 0

    # Iterate through the string
    while index < len(string):
        # Check if the current substring matches the lowercase word "hello"
        if string[index:index + len(word)] == word:
            count += 1

            # Move the index to the end of the current occurrence of "hello"
            index += len(word)
        else:
            # Move the index to the next character
            index += 1

    # Check if the count is greater than 0
    if count > 0:
        return True, count
    else:
        return False, count