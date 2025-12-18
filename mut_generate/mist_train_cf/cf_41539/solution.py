"""
QUESTION:
Write a function `countEmptyDivsWithClass` that takes a string `htmlCode` representing the HTML code and returns the count of empty div elements with the class "help-block text-danger". The function should only count div elements with no content (i.e., the closing div tag immediately follows the opening div tag) and exactly the class "help-block text-danger". The function should be case-sensitive and consider the exact class name.
"""

def countEmptyDivsWithClass(htmlCode: str) -> int:
    count = 0
    start = 0
    while True:
        start = htmlCode.find('<div class="help-block text-danger">', start)
        if start == -1:
            break
        end = htmlCode.find('</div>', start)
        if end == -1:
            break
        if htmlCode[start:end].strip() == '<div class="help-block text-danger"></div>':
            count += 1
        start = end + 6  # Skip the length of '</div>'
    return count