"""
QUESTION:
Design a function named `count_substring_occurrences` that takes two parameters, `string` and `substring`, and returns the number of occurrences of `substring` in `string` where `substring` is a separate word. 

The function should have a time complexity of O(n), where n is the length of the `string`, and a space complexity of O(1), excluding the space required for the input and output.
"""

def count_substring_occurrences(string, substring):
    # Initialize the count to 0
    count = 0

    # Convert the string and substring to lowercase
    string = string.lower()
    substring = substring.lower()

    # Split the string into words
    words = string.split()

    # Iterate through each word in the string
    for word in words:
        # If the word is the same as the substring, increment the count
        if word == substring:
            count += 1

    return count