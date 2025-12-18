"""
QUESTION:
Write a Python function `extract_package_info` that takes two parameters: `REQUIREMENTS` (a list of requirements) and `LONG_DESCRIPTION` (a string containing a package description). The function should extract the package version, requirements, and author's email address from these inputs. The version and author's email address should be extracted from `LONG_DESCRIPTION` using regular expressions. The function should return a dictionary with keys "version", "requirements", and "author_email". If the version or email address is not found, the corresponding dictionary value should be "Version not found" or "Email not found".
"""

import re

def extract_package_info(REQUIREMENTS, LONG_DESCRIPTION):
    package_info = {}

    # Extract version number from LONG_DESCRIPTION using regular expression
    version_match = re.search(r"version='(.*?)'", LONG_DESCRIPTION)
    if version_match:
        package_info['version'] = version_match.group(1)
    else:
        package_info['version'] = "Version not found"

    # Extract requirements from REQUIREMENTS
    package_info['requirements'] = REQUIREMENTS

    # Extract author's email address from LONG_DESCRIPTION using regular expression
    email_match = re.search(r'author_email=\'(.*?)\'', LONG_DESCRIPTION)
    if email_match:
        package_info['author_email'] = email_match.group(1)
    else:
        package_info['author_email'] = "Email not found"

    return package_info