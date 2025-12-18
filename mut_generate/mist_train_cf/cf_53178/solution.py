"""
QUESTION:
Write a function named `styled_text` that takes three parameters: `text`, `style`, and `size`, `color`, and returns a string of HTML that formats the `text` with the specified `style`, `size`, and `color`. The `style` parameter should be one of the valid CSS font styles, the `size` parameter should be a valid CSS font size, and the `color` parameter should be a valid CSS color.
"""

def styled_text(text, style='normal', size='1rem', color='black'):
    return f'<p style="font-style: {style}; font-size: {size}; color: {color}">{text}</p>'