"""
QUESTION:
Create a function `get_unique_combinations` that takes a string of characters as an argument and returns a list of all unique combinations of characters possible, excluding any combination that includes a repeating character.
"""

def get_unique_combinations(string):
    unique_combinations = []
    length = len(string)
    for i in range(length):
        unique_combinations.append(string[i])
        for j in range(i+1, length):
            substring = string[i:j+1]
            if len(set(substring)) == len(substring):
                unique_combinations.append(substring)
    return unique_combinations