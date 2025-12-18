"""
QUESTION:
Create a function `extract_copyright_info` that takes a string `text` as input and returns a dictionary containing the extracted copyright information. The copyright notice format includes a date in the format "Month Day Year", a copyright holder on the line following the date, and a license starting with "Licensed under the" keyword. The date, copyright holder, and license information are always present, and the date is always in the specified format. The copyright holder and license information may span multiple lines.
"""

import re

def extract_copyright_info(text: str) -> dict:
    copyright_info = {}
    lines = text.split('\n')
    copyright_info["date"] = lines[0].strip()
    copyright_holder = lines[1].strip()
    for line in lines[2:]:
        if line.lstrip().startswith("Licensed under the"):
            copyright_info["license"] = line.lstrip("Licensed under the").strip()
            break
        else:
            copyright_holder += " " + line.strip()
    copyright_info["copyright_holder"] = copyright_holder

    return copyright_info