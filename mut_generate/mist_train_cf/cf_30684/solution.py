"""
QUESTION:
Create a function `extract_ui_details` that takes a code snippet as input and returns a dictionary containing the extracted UI window details. The dictionary should include the following keys:
- "window_name": the name of the UI window being created
- "window_width": the width of the UI window
- "window_title": the title of the UI window
- "scroll_height": the height of the scroll area within the UI window

The input code snippet is a string that contains PyMEL code for creating a UI window. The function should use regular expressions to extract the required information from the code snippet. If a detail is not found in the code snippet, it should not be included in the returned dictionary.
"""

import re

def extract_ui_details(code_snippet):
    details = {}
    
    # Extract window name
    window_name_match = re.search(r'pm\.window\(\s*\"(.+?)\"', code_snippet)
    if window_name_match:
        details["window_name"] = window_name_match.group(1)
    
    # Extract window width
    window_width_match = re.search(r'width\s*=\s*(\d+)', code_snippet)
    if window_width_match:
        details["window_width"] = int(window_width_match.group(1))
    
    # Extract window title
    window_title_match = re.search(r'title\s*=\s*\"(.+?)\"', code_snippet)
    if window_title_match:
        details["window_title"] = window_title_match.group(1)
    
    # Extract scroll height
    scroll_height_match = re.search(r'scrollHight\s*=\s*(\d+)', code_snippet)
    if scroll_height_match:
        details["scroll_height"] = int(scroll_height_match.group(1))
    
    return details