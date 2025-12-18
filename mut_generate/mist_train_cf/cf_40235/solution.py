"""
QUESTION:
Write a function `countTagOccurrences(html, tagName, attribute, value)` that takes in an HTML string `html` and counts the occurrences of a specific HTML tag `tagName` with a given `attribute` and `value`. The function should return the count of occurrences of the specified tag with the given attribute and value. The input strings `html`, `tagName`, `attribute`, and `value` are of lengths 1 to 10^5, 1 to 50, 1 to 50, and 1 to 50, respectively.
"""

def countTagOccurrences(html, tagName, attribute, value):
    count = 0
    tag_start = "<" + tagName
    tag_end = "</" + tagName + ">"
    index = 0
    while index < len(html):
        start = html.find(tag_start, index)
        if start == -1:
            break
        end = html.find(">", start)
        tag = html[start:end+1]
        if attribute in tag and value in tag:
            count += 1
        index = end + 1
    return count