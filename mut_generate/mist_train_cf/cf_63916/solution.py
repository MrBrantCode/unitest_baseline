"""
QUESTION:
Create a function called `evaluate_string` that takes a string `s` as input and returns either a list of phrases or an integer. If `s` contains semicolons or double colons, return a list of phrases separated by these characters. Otherwise, return the cumulative sum of uppercase alphabetical symbols with even indices (where 'A' has an index of 0, 'B' has an index of 1, and so on) in the string.
"""

def evaluate_string(s):
    # check for semicolons or double colons in string 
    if ";" in s or "::" in s:
        # splitting the string on semicolons and double colons
        s = s.replace("::", ";")
        return s.split(";")
    else:
        cumulative_sum = 0
        for letter in s:
            if letter.isupper():
                if ord(letter) % 2 == 0:
                    cumulative_sum += 1
        return cumulative_sum