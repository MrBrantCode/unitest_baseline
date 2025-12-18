"""
QUESTION:
Create a function `parseSidebarMenu(html)` that takes an HTML string as input, extracts the URLs and their corresponding labels from a given sidebar menu, and returns a list of tuples. Each tuple should contain the URL and label of a menu item. Assume the HTML structure is consistent with each menu item represented by a `<div>` element with the class "sidebar-item" containing an `<a>` element, where the URL is the `href` attribute and the label is the text content of the `<a>` element.
"""

import re

def parseSidebarMenu(html):
    menu_items = re.findall(r'<div class="sidebar-item"><a href="([^"]+)".*?>(.*?)</a></div>', html)
    return menu_items