"""
QUESTION:
Write a function `checkMentalHealthIcon` that takes an HTML snippet as input and returns "Mental health icon found" if the snippet contains a `<span>` element with class `fas fa-brain`, and "Mental health icon not found" otherwise. The function should be case-sensitive and should not consider any other elements or attributes besides the specified class in the `<span>` element.
"""

import re

def checkMentalHealthIcon(html_snippet):
    # Define the pattern to match the mental health icon element
    pattern = r'<span class\s*=\s*["\']fas fa-brain["\'].*>.*</span>'
    
    # Use regular expression to search for the pattern in the HTML snippet
    if re.search(pattern, html_snippet):
        return "Mental health icon found"
    else:
        return "Mental health icon not found"