"""
QUESTION:
Write a function named `reverseWords` that takes a string `input_string` as input and returns a string where the order of words is reversed, without any leading or trailing spaces. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def reverseWords(input_string):
    input_string = input_string.strip()
    input_string = input_string[::-1]
    start = 0
    end = 0
    while end < len(input_string):
        while end < len(input_string) and input_string[end] != ' ':
            end += 1
        input_string = input_string[:start] + input_string[start:end][::-1] + input_string[end:]
        start = end + 1
        end = start
    return input_string