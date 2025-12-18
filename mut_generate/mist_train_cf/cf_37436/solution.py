"""
QUESTION:
Write a function `parse_svg_data(svg_code: str) -> dict` that takes a string `svg_code` as input, representing the SVG elements from a web application. The function should parse the SVG code and extract the data related to the number of registered users and total earnings, represented by two `<svg>` elements with a `<text>` element containing the relevant data. The function should return a dictionary with the extracted data in the format: `{"total_users": <number of registered users>, "total_earnings": <total earnings as a float>}`. Assume the number of registered users is an integer and the total earnings are a currency value.
"""

import re

def parse_svg_data(svg_code: str) -> dict:
    total_users_match = re.search(r'<text.*?>(\d+)</text>', svg_code)
    total_earnings_match = re.search(r'<text.*?>(\$[\d,]+\.\d+)</text>', svg_code)

    total_users = int(total_users_match.group(1))
    total_earnings = float(total_earnings_match.group(1).replace('$', '').replace(',', ''))

    return {
        "total_users": total_users,
        "total_earnings": total_earnings,
    }