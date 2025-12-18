"""
QUESTION:
Write a function `extractDocumentContent` that takes a string representing a document and returns the content within the comment block as a string, preserving the original formatting. The comment block is denoted by the opening delimiter `/*` and the closing delimiter `*/`. If no comment block is found, return a specific message.
"""

def extractDocumentContent(document):
    start_index = document.find("/*") + 2
    end_index = document.find("*/")
    if start_index != -1 and end_index != -1:
        return document[start_index:end_index].strip()
    else:
        return "No comment block found in the document."