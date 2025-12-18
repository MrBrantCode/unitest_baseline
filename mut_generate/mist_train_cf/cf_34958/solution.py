"""
QUESTION:
Write a function `extract_php_sections` that takes a string of PHP code as input and returns the content within all PHP sections. The content within PHP sections is defined as the text between `<?php` and `?>` tags, including leading and trailing whitespace. If there are multiple PHP sections in the input string, the function should return a list of all the extracted content.
"""

import re

def extract_php_sections(php_code):
    php_sections = re.findall(r'<?php(.*?)\?>', php_code, re.DOTALL)
    return [section.strip() for section in php_sections]