"""
QUESTION:
Write a function `countCommentLines` that takes a string as input and returns the number of lines in the comment block. The comment block starts with a line containing "//------------------------------------------------------------------------------" and ends with a line containing "//" followed by any number of spaces and then a closing curly brace "}". The input string will contain the comment block and possibly other lines before or after it. The function should return the number of lines in the comment block, excluding the start and end lines.
"""

def countCommentLines(comment_block):
    lines = comment_block.split('\n')
    start_index = lines.index('//------------------------------------------------------------------------------')
    end_index = lines.index(next(line for line in reversed(lines) if line.strip().startswith('// }')))
    return end_index - start_index - 1