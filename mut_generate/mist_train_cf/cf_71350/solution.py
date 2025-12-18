"""
QUESTION:
Write a function `lengthLongestPath` that takes a string `input` representing a file system and returns a tuple containing the length of the longest absolute path to a file, the size of the file, and the file type (extension). The function should handle nested directories and files with sizes. If there is no file in the system, return `0`, `0`, and `None` respectively.

The input string is in the format of a tree-like structure, where each directory and file is represented as a line, and the indentation level of the line represents the depth of the directory or file in the tree. Each file name is followed by its size in bytes. The function should parse this string and return the required information.
"""

def lengthLongestPath(input):
    maxlen = maxsize = 0
    maxtype = None
    path = []
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            name, size = name.rsplit(' ', 1)
            size = int(size)
            maxlen = max(maxlen, len('/'.join(path[:depth]) + '/' + name))
            if size > maxsize:
                maxsize = size
                maxtype = name.rsplit('.', 1)[-1]
        else:
            while len(path) > depth:
                path.pop()
            path.append(name)
    return maxlen if maxlen > 0 else 0, maxsize if maxsize > 0 else 0, maxtype