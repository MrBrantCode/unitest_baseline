"""
QUESTION:
Design a function `filter_strings(lst)` that takes a list of strings as input and returns a new list containing only the strings that do not have the phrases "regardless of" or "in spite of" (case-insensitive). The function should use character comparison instead of Python's inbuilt string methods to check for the phrases.
"""

def filter_strings(lst):
    new_list = []
    phrases = ["regardless of", "in spite of"]
    for string in lst:
        string = string.lower()
        include = True
        for phrase in phrases:
            i = 0
            while i <= len(string) - len(phrase):
                window_string = string[i:i+len(phrase)]
                if window_string == phrase:
                    include = False
                    break
                i += 1
            if include == False:
                break
        if include:
            new_list.append(string)
    return new_list