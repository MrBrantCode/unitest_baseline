"""
QUESTION:
Write a function named `check_and_count_hello` that takes a string as input and returns a boolean value indicating whether the string contains the word "hello" (case-insensitive) and an integer representing the number of occurrences of the word "hello" in the string. The function should handle overlapping occurrences and have a time complexity of O(n), where n is the length of the string.
"""

def check_and_count_hello(string):
    string = string.lower()  
    word = "hello"
    count = 0
    index = 0
    
    while index < len(string):
        if string[index:index+len(word)] == word:  
            count += 1
            index += len(word)  
        else:
            index += 1
    
    return count > 0, count