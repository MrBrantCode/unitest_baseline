"""
QUESTION:
Create a function `extractLicenseInfo(text: str)` that takes a string `text` as input. The function should extract license information from the text if it exists, and return it as a dictionary where the keys are the license keys and the values are the corresponding license values. The license information is enclosed within a comment block that starts with `/*` and ends with `*/`, and each key-value pair is separated by a colon (`:`). If no license information is found, the function should return the string "No license information found".
"""

from typing import Dict, Union

def extract_license_info(text: str) -> Union[Dict[str, str], str]:
    start_comment = '/*'
    end_comment = '*/'
    start_index = text.find(start_comment)
    end_index = text.find(end_comment)

    if start_index != -1 and end_index != -1:
        comment_block = text[start_index + len(start_comment):end_index].strip()
        lines = comment_block.split('\n')
        license_info = {}
        for line in lines:
            if ':' in line:
                key, value = map(str.strip, line.split(':', 1))
                license_info[key] = value
        if license_info:
            return license_info
        else:
            return "No license information found"
    else:
        return "No license information found"