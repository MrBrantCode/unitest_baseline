"""
QUESTION:
Create a function `extractRepoAndQuote` that takes a string input, extracts the repository name and the quote from the string, and returns a list of tuples. The repository name is located between the angle brackets `< >` and the quote is enclosed within double forward slashes `//` and `—`. The function should be able to handle multiple occurrences of the repository name and quote in the input.
"""

import re

def extractRepoAndQuote(input_str):
    pattern = r'<(.*?)>(.*?)//\s*“(.*?)”\s*—\s*(.*?)\n'
    matches = re.findall(pattern, input_str)
    result = [(match[0], f'“{match[2]}” — {match[3]}') for match in matches]
    return result