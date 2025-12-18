"""
QUESTION:
Write a function `count_word` that takes two parameters: a string `string` and a word `word`. Return the number of occurrences of `word` in `string` excluding any occurrences within parentheses.
"""

def count_word(string, word):
    count = 0
    inside_parentheses = False
    current_word = ""
    for char in string:
        if char == "(":
            inside_parentheses = True
        elif char == ")":
            inside_parentheses = False
        elif char.isalpha():
            current_word += char.lower()
        elif char == ' ':
            if current_word == word.lower() and not inside_parentheses:
                count += 1
            current_word = ""
        else:
            current_word = ""
    if current_word == word.lower() and not inside_parentheses:
        count += 1
    return count