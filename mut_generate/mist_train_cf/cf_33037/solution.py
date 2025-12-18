"""
QUESTION:
Create a function `countCSSClasses(html)` that takes a string of HTML as input and returns a dictionary where the keys are unique CSS classes and the values are the frequencies of their occurrences. The function should only count CSS classes within the `class` attribute of HTML tags.
"""

import re

def countCSSClasses(html):
    class_pattern = r'class="([^"]+)"'
    classes = re.findall(class_pattern, html)
    class_counts = {}
    for css_class in classes:
        for single_class in css_class.split():
            if single_class in class_counts:
                class_counts[single_class] += 1
            else:
                class_counts[single_class] = 1
    return class_counts