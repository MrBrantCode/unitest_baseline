"""
QUESTION:
Create a function `extractJavaScript` that takes a string `html` representing HTML content and returns a list of JavaScript code snippets found within the `<script>` tags, excluding any JavaScript code within `<script>` tags that are part of a template engine (i.e., containing the substring `@push`).
"""

import re

def extractJavaScript(html):
    script_tags = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
    filtered_scripts = [script for script in script_tags if '@push' not in script]
    return filtered_scripts