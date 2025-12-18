"""
QUESTION:
Create a function named `replace_keyword` that takes a string and two words (a keyword and a replacement word) as input. This function should find all occurrences of the keyword in the string, ignoring those that are part of another word, and replace them with the replacement word. The function should also count the total number of replaced occurrences. The function must be case-sensitive, have a time complexity of O(n), and a space complexity of O(1), where n is the length of the input string.
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