"""
QUESTION:
Write a function called `tokenize_string` that takes an input string and returns a dictionary with three keys: "alphabet", "digit", and "symbol". The values corresponding to each key should be a list of unique characters in the input string that fall into the respective category. The function should run in O(n) time complexity, where n is the length of the input string.
"""

def tokenize_string(string):
    groups = {
        "alphabet": [],
        "digit": [],
        "symbol": []
    }
    seen = set()
    for char in string:
        if char.isalpha():
            if char not in seen:
                groups["alphabet"].append(char)
                seen.add(char)
        elif char.isdigit():
            if char not in seen:
                groups["digit"].append(char)
                seen.add(char)
        else:
            if char not in seen:
                groups["symbol"].append(char)
                seen.add(char)
    return groups