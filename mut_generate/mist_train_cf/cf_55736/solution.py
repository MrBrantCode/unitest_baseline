"""
QUESTION:
Create a function called `mystery(code)` that takes a string `code` as input. If `code` is not a string, the function should return the error message "Invalid input". The function should return a dictionary where the keys are unique words in `code` separated by spaces or semicolons. If no spaces or semicolons exist in `code`, the keys should be uppercase letters at even indexes. The values in the dictionary should be the occurrence of each key in `code`.
"""

def mystery(code):
    if not isinstance(code, str):
        return "Invalid input"

    d = {}
    code = code.replace(';', ' ')

    for word in code.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    if len(d) == 0:
        for i in range(0, len(code), 2):
            if code[i].isalpha() and code[i].isupper():
                if code[i] in d:
                    d[code[i]] += 1
                else:
                    d[code[i]] = 1

    return d