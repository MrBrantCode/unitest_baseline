"""
QUESTION:
Create a function called `extract_first_last_words` that takes in an array of strings, where each string can have up to 100 characters and the array can contain up to 100 strings. The function should return an array of tuples, where each tuple contains the first and last word of the corresponding string in the input array, ignoring any leading or trailing whitespace in each string. If a string contains only one word, the function should return a tuple with the same word twice. If the input array is empty, the function should return an empty array.
"""

def extract_first_last_words(arr):
    result = []
    for string in arr:
        string = string.strip()
        words = string.split()

        if len(words) == 0:
            result.append(("", ""))
        elif len(words) == 1:
            result.append((words[0], words[0]))
        else:
            result.append((words[0], words[-1]))

    return result