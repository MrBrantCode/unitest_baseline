"""
QUESTION:
Create a function named `replace_keyword` that takes a string, a keyword, and a replacement word as input. The function should replace all occurrences of the keyword in the string with the replacement word, ignoring any occurrences that are part of another word. The function should be case-sensitive and return the total number of occurrences of the keyword and the modified string. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

def replace_keyword(string, keyword, replacement):
    count = 0
    i = 0
    while i < len(string):
        if string[i:i+len(keyword)] == keyword:
            # Check if the keyword is part of another word
            if (i > 0 and string[i-1].isalpha()) or (i+len(keyword) < len(string) and string[i+len(keyword)].isalpha()):
                i += 1
                continue
            # Replace the keyword with the replacement word
            string = string[:i] + replacement + string[i+len(keyword):]
            count += 1
            i += len(replacement)
        else:
            i += 1
    return count, string