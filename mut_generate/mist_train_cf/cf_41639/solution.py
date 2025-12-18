"""
QUESTION:
Write a function named `extract_script_info` that takes a script string as input and returns a tuple containing the function call with its arguments and the summary comment block content. The function call should be the first occurrence of a string that matches the pattern of a function name followed by arguments enclosed in parentheses, and the summary comment block content should be the text enclosed in the first `<summary>` and `</summary>` tags. The function should use regular expressions to extract the required information.
"""

import re

def extract_script_info(script):
    # Extract function call using regex
    function_call = re.search(r'(\w+)\((.*?)\)', script).group(0)

    # Extract summary comment block content using regex
    summary_content = re.search(r'<summary>(.*?)</summary>', script, re.DOTALL).group(1).strip()

    return function_call, summary_content