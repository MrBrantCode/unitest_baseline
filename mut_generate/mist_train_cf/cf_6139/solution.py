"""
QUESTION:
Create a function `contains_hello` that takes a string as input and returns a tuple containing a boolean indicating whether the string contains the word "hello" (case-insensitive) and the number of times "hello" appears in the string. The function should have a time complexity of O(n), where n is the length of the string, and should not use built-in string manipulation functions such as `str.lower()` or `str.count()`.
"""

def contains_hello(string):
    word = "hello"
    count = 0
    index = 0

    while index < len(string):
        match = True
        for i in range(len(word)):
            if index + i >= len(string) or string[index + i].lower() != word[i]:
                match = False
                break
        if match:
            count += 1
            index += len(word)
        else:
            index += 1

    return (count > 0), count