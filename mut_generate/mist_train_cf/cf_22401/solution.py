"""
QUESTION:
Write a function `modify_paragraph` that takes a string `paragraph` as input and returns a modified string. The function should replace all instances of "the" with "a" and all instances of "is" with "was" in the given paragraph.
"""

def modify_paragraph(paragraph):
    return paragraph.replace("the", "a").replace("is", "was")