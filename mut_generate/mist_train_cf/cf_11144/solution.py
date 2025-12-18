"""
QUESTION:
Write a function `increase_font_size(html)` that increases the font size of each paragraph in the given HTML from 12px to 24px, preserving the original formatting and styling. The function should not use any additional data structures, resulting in a space complexity of O(1), and should complete in O(n) time complexity, where n is the total number of characters in all paragraphs combined.
"""

def entance(html):
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