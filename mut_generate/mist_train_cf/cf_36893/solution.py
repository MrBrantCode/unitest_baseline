"""
QUESTION:
Implement the function `extract_info(code_snippet: str) -> dict` to parse a given code snippet and extract the author and license information. The code snippet will be a multi-line string in the format:
```
'''
    author='<AUTHOR_NAME>',
    license='<LICENSE_TYPE>',
)
'''
```
Return a dictionary containing the extracted author and license information. If the code snippet does not follow the specified format, return an empty dictionary.
"""

import re

def extract_info(code_snippet: str) -> dict:
    pattern = r"author='(.*?)',\s*license='(.*?)',\s*\)"
    match = re.search(pattern, code_snippet)
    if match:
        author = match.group(1)
        license_type = match.group(2)
        return {'author': author, 'license': license_type}
    else:
        return {}