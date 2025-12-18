"""
QUESTION:
Implement the function `parseHTMLStructure(code: str) -> str` that takes a string `code` representing the HTML code snippet and returns the hierarchical representation of the HTML structure. The HTML structure consists of nested elements, each represented by an opening tag, a content block, and a closing tag. The function should return a string where each line represents a level of nesting, and the indentation indicates the parent-child relationship between the HTML elements. The input `code` string may contain multiple levels of nested HTML elements, and the function should handle these nested elements correctly.
"""

def parseHTMLStructure(code: str) -> str:
    stack = []
    result = ""
    i = 0
    while i < len(code):
        if code[i] == "<":
            j = i
            while code[j] != ">":
                j += 1
            tag = code[i+1:j]
            if tag[0] != "/":
                if stack:
                    result += "    " * len(stack) + tag + "\n"
                else:
                    result += tag + "\n"
                stack.append(tag)
            else:
                stack.pop()
            i = j
        i += 1
    return result