"""
QUESTION:
Write a function `extract_license_info(code: str) -> dict` that takes a string `code` representing a code snippet as input and returns a dictionary containing the extracted license information. The code snippet may contain multiple comments, and the license information may be present in any of them. The license information will be in the following format: "Licensed under the {license_type} License, Version {version_number}". The function should return a dictionary with keys "license_type", "version", and "additional_info" representing the type of license, the version number of the license, and any additional information found within the comment containing the license information, respectively.
"""

import re

def extract_license_info(code: str) -> dict:
    license_info = {}
    pattern = r'Licensed under the (.*?) License, Version (\d+\.\d+)'
    match = re.search(pattern, code)
    if match:
        license_info["license_type"] = match.group(1)
        license_info["version"] = match.group(2)
        comment_lines = code.split('\n')
        for line in comment_lines:
            if match.group(0) in line:
                additional_info = []
                for line in comment_lines[comment_lines.index(line)+1:]:
                    if line.strip().startswith('#'):
                        additional_info.append(line.lstrip('#').strip())
                    else:
                        break
                license_info["additional_info"] = '\n'.join(additional_info)
                break
    return license_info