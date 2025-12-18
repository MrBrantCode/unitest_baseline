"""
QUESTION:
Write a function `calculateTotalHeight` that takes a string representing an HTML template as input and returns a list of total heights for each list item. The total height for each list item is the sum of the heights of all the div elements within that list item. The function should be able to handle any number of list items and div elements with varying heights. The input HTML template is a string and the output should be a list of integers representing the total height for each list item.
"""

from typing import List
import re

def calculateTotalHeight(html_template: str) -> List[int]:
    total_heights = []
    list_items = re.findall(r'<li>.*?</li>', html_template, re.DOTALL)
    for item in list_items:
        div_heights = re.findall(r'style="height: (\d+)px"', item)
        total_height = sum(map(int, div_heights))
        total_heights.append(total_height)
    return total_heights