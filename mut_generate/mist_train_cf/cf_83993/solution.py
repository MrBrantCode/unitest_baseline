"""
QUESTION:
Write a function named `transform_string` that takes a string `s` as input and returns a string where all occurrences of one or more consecutive whitespaces are replaced with a single whitespace and all occurrences of one or more consecutive underscores are replaced with a single underscore. Then, replace all underscores with spaces and all spaces with underscores. The function should handle strings containing any characters.
"""

def transform_string(s):
    s = re.sub('_+', '_', s)
    s = re.sub(' +', ' ', s)
    trans = s.maketrans('_ ', ' _')
    return s.translate(trans)