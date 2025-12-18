"""
QUESTION:
Write a Python function `extract_info_from_code(code: str) -> dict` that takes a Python code snippet as input, extracts the version number, package name, contact email, homepage URL, and repository URL, and returns them in a dictionary with the keys "version", "package_name", "contact_email", "homepage_url", and "repository_url". The function should handle the version number as a tuple of integers and strings. The input code snippet is expected to be in a format similar to the provided example.
"""

import re

def extract_info_from_code(code: str) -> dict:
    info_dict = {}
    version_match = re.search(r'VERSION = \((.*?)\)', code)
    if version_match:
        info_dict["version"] = tuple(map(int, version_match.group(1).split(', ')))
    info_dict["package_name"] = re.search(r'__package_name__ = \'(.*?)\'', code).group(1)
    info_dict["contact_email"] = re.search(r'__contact_emails__ = \'(.*?)\'', code).group(1)
    info_dict["homepage_url"] = re.search(r'__homepage__ = \'(.*?)\'', code).group(1)
    info_dict["repository_url"] = re.search(r'__repository_url__ = \'(.*?)\'', code).group(1)

    return info_dict