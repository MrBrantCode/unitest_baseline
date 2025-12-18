"""
QUESTION:
Write a function `detect_quotes(string)` that takes a string as input and returns a message. The function should check if there are at least two double quotes in the string. If there are, return the message "Double quotes already present in string". Otherwise, return a list of indices of all single quotes in the string.
"""

def detect_quotes(string):
    double_quote_count = 0
    single_quote_indices = []
    for i in range(len(string)):
        if string[i] == "\"":
            double_quote_count += 1
        elif string[i] == "'":
            single_quote_indices.append(i)
    if double_quote_count >= 2:
        return "Double quotes already present in string"
    else:
        return single_quote_indices