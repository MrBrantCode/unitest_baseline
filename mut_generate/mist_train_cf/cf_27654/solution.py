"""
QUESTION:
Implement the function `extract_license(comments: List[str]) -> Optional[str]` which takes a list of strings representing code comments and returns the extracted license text if found, or `None` if no license information is present. The function should identify the license text as consecutive lines starting with `#` and the first line containing two or fewer spaces after the `#` symbol.
"""

from typing import List, Optional

def extract_license(comments: List[str]) -> Optional[str]:
    license_text = []
    license_started = False

    for comment in comments:
        if comment.strip().startswith('#'):
            if not license_started and comment.strip().count(' ') <= 2:
                license_started = True
            if license_started:
                license_text.append(comment.lstrip('#').strip())
        else:
            if license_started:
                break

    if license_text:
        return '\n'.join(license_text)
    else:
        return None