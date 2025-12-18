"""
QUESTION:
Write a function `extract_total_price(html_code)` that takes a string `html_code` as input and returns the total price as a floating-point number enclosed within the `{{globleCartData.total_price|currency:" "}}` tag in the HTML code. The function should return `None` if no match is found. The total price will be a valid floating-point number.
"""

import re

def entrance(html_code):
    pattern = r'{{globleCartData.total_price\|currency:" "\}}(\d+\.\d+)'
    match = re.search(pattern, html_code)
    if match:
        total_price = float(match.group(1))
        return total_price
    else:
        return None