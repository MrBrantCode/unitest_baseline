"""
QUESTION:
Create a function called `replace_and_count` that takes three parameters: a string, a keyword, and a replacement word. The function should replace all whole word occurrences of the keyword in the string with the replacement word and return the modified string along with the total count of occurrences. The function should be case-sensitive and consider only whole word matches, ignoring occurrences of the keyword within other words.
"""

def replace_and_count(string, keyword, replacement):
    count = 0
    words = string.split()
    for i in range(len(words)):
        if words[i] == keyword:
            words[i] = replacement
            count += 1
    new_string = ' '.join(words)
    return new_string, count