"""
QUESTION:
Design a function named `underscore_spaces` that replaces all spaces with underscores in a given text string, but only in words that are not part of a specific set of programming languages' syntax. The function should be able to identify and ignore spaces within the syntax of programming languages such as Python, Java, C++, JavaScript, and Ruby. It should also be able to handle and preserve SQL queries, CSS and HTML tags, JSON and XML objects, LaTeX syntax, and markdown syntax within the text, without altering the spaces within these structures. Note that the function is not required to be perfect and can use a simplified approach, but it should demonstrate some proficiency in handling different programming languages and syntax.
"""

def underscore_spaces(text):
    keywords = [
        # Add more programming keywords here
        'if', 'else', 'while', 'for', 'return', 
        'int', 'float', 'def', 'class', 'public', 
        'private', 'protected'
    ]
    series = []
    current_word = ''
    
    for c in text:
        if c == ' ':
            if current_word not in keywords:
                current_word = current_word.replace(' ', '_')
            series.append(current_word)
            current_word = ''
        else:
            current_word += c
    if current_word not in keywords:
        current_word = current_word.replace(' ', '_')
    series.append(current_word)

    return ' '.join(series)