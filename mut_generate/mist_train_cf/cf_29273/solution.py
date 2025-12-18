"""
QUESTION:
Create a function `parseHeaders` that takes an HTTP request headers string as input and returns a dictionary containing the extracted header names and their corresponding values. The input string consists of key-value pairs, where keys are double-quoted header names and values are strings, separated by a colon and space. The function should handle cases where the input string may contain additional headers beyond the specified ones and correctly extract the specified headers regardless of their order in the input string.
"""

def parseHeaders(headers_str):
    headers = {}
    lines = headers_str.split("\n")
    for line in lines:
        if line.strip():  # Check if the line is not empty
            key, value = line.split(": ", 1)
            key = key.strip('"')  # Remove double quotes from the key
            headers[key] = value
    return headers