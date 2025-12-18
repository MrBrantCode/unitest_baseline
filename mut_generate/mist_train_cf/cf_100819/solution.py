"""
QUESTION:
Write a function `detect_quotes` that takes a string as an argument and returns a message indicating whether a pair of double quotes are already present in the string. If not, return a message with a list of indices of single quotes in the string.
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
        return f"Single quote indices: {single_quote_indices}"