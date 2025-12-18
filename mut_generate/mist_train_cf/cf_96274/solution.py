"""
QUESTION:
Write a function `check_and_count_hello` that takes a string as input and returns a tuple containing a boolean indicating whether the string contains the word "hello" (case-insensitive) and the number of times "hello" appears in the string. The function should have a time complexity of O(n), where n is the length of the string, and should handle overlapping occurrences of "hello".
"""

def check_and_count_hello(string):
    string = string.lower()  # convert the string to lowercase for case-insensitive comparison
    word = "hello"
    count = 0
    index = 0
    
    while index < len(string):
        if string[index:index+len(word)] == word:  # check if the substring matches the word
            count += 1
            index += len(word)  # skip to the next index after the matched word
        else:
            index += 1
    
    return count > 0, count