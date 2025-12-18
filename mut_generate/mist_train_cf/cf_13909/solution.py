"""
QUESTION:
Implement a function `substring_search` that takes two parameters: `string` and `substring`. The function should perform a case-insensitive search for the `substring` in the `string` and return the index of the first occurrence where the `substring` is not surrounded by other alphanumeric characters. If no such occurrence is found, return -1.
"""

def substring_search(string, substring):
    string = string.lower()  
    substring = substring.lower()
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            if (i == 0 or not string[i-1].isalnum()) and (i+len(substring) == len(string) or not string[i+len(substring)].isalnum()):
                return i
    
    return -1  