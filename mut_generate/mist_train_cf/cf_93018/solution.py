"""
QUESTION:
Implement the function `substring_search(string, substring)` to find the index of the first occurrence of a substring within a given string. The search should be case-insensitive and the substring should be considered a match only if it is not surrounded by other alphanumeric characters. If the substring is not found or does not meet the requirements, return -1.
"""

def substring_search(string, substring):
    string = string.lower()  
    substring = substring.lower()
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            if (i == 0 or not string[i-1].isalpha()) and (i+len(substring) == len(string) or not string[i+len(substring)].isalpha()):
                return i
    
    return -1