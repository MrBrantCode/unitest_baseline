"""
QUESTION:
Create a function `count_alphanumeric(s)` that calculates the frequency of each alphanumeric character in a given string `s`. The function should return a dictionary where the keys are the alphanumeric characters and the values are their corresponding counts. The function should ignore non-alphanumeric characters and consider uppercase and lowercase letters as distinct characters.
"""

def count_alphanumeric(s):
    count_dict = {}
    for c in s:
        if c.isalnum():
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1
    return count_dict