"""
QUESTION:
Implement a function `treeStats` that takes a string of ASCII art representing a stylized tree as input and returns a dictionary containing the tree's statistics. The input string consists of multiple lines, each representing a level of the tree, and only contains spaces, underscores, vertical bars, and backslashes. The function should return a dictionary with the following keys: "height" (the number of levels in the tree), "width" (the width of the tree at its widest point), and "leaves" (the number of occurrences of the character "|").
"""

def treeStats(ascii_art):
    lines = ascii_art.split('\n')
    height = len(lines)
    width = max(len(line) for line in lines)
    leaves = sum(line.count('|') for line in lines)
    return {"height": height, "width": width, "leaves": leaves}