"""
QUESTION:
Write a function `increase_font_size(html)` that takes a string of HTML as input and returns the modified HTML with the font size of each paragraph increased from 12px to 24px, preserving the original formatting and styling. The solution should not use any third-party libraries or frameworks, and it should meet the following requirements: 
- Time Complexity: O(n), where n is the total number of characters in all paragraphs combined.
- Space Complexity: O(1), meaning no additional data structures should be used to solve the problem.
"""

def increase_font_size(html):
    lines = html.split('\n')
    inside_paragraph = False
    for i in range(len(lines)):
        line = lines[i]
        if '<p' in line:
            inside_paragraph = True
            line = line.replace('font-size: 12px', 'font-size: 24px')
        elif '</p' in line:
            inside_paragraph = False
        if inside_paragraph:
            line = line.replace('font-size: 12px', 'font-size: 24px')
        lines[i] = line
    modified_html = '\n'.join(lines)
    return modified_html