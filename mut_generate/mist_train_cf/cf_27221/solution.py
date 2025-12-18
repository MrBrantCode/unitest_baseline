"""
QUESTION:
Create a function `countElementOccurrences(html, targetElement)` that takes two parameters: 
- `html` (string) representing the input HTML code, 
- `targetElement` (string) representing the target HTML element tag. 

The function should return the count of occurrences of the `targetElement` within the `html` string. The function must handle nested HTML elements and should be case-sensitive.
"""

def countElementOccurrences(html, targetElement):
    count = 0
    start_index = 0
    while True:
        next_index = html.find("<" + targetElement, start_index)
        if next_index == -1:
            break
        count += 1
        start_index = next_index + 1
    return count