"""
QUESTION:
Write a function named `extract_comments` that takes a string of Python source code as input and returns a list of extracted comments. The function should only consider comments that start with the '#' symbol, ignoring any '#' symbols within strings. It should not detect comments inside triple quotes. The function should return a list of comments with leading and trailing whitespace stripped.
"""

def extract_comments(source_code):
    lines = source_code.split('\n')
    comments = []

    for line in lines:
        if '#' in line:
            # Split the line into code and comment
            code, comment = line.split('#', 1)

            # Ignore hash symbols within strings 
            if '"' in code or "'" in code:  
                continue  
            
            # If the comment is not empty then append to the list
            if comment.strip():  
                comments.append(comment.strip())

    return comments