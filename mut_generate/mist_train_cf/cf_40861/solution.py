"""
QUESTION:
Write a function `extract_license_info(file_content: str) -> str` that takes a string `file_content` as input, representing the content of a file. The function should extract the license information from the file content and return it as a string. The license information is always enclosed within a comment block that starts with a '#' character and ends with an empty line or a non-comment line. If the file content does not contain any license information, the function should return "No license information found".
"""

def extract_license_info(file_content: str) -> str:
    lines = file_content.strip().split('\n')
    license_info = []
    in_license_block = False

    for line in lines:
        if line.startswith('#'):
            if in_license_block:
                license_info.append(line.lstrip('#').strip())
            else:
                in_license_block = True
                license_info.append(line.lstrip('#').strip())
        else:
            if in_license_block:
                break

    if license_info:
        return '\n'.join(license_info)
    else:
        return "No license information found"