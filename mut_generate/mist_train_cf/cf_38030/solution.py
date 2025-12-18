"""
QUESTION:
Create a function named `extract_license_types` that takes a list of strings as input where each string represents a line from a software license comment. The function should return a list of license types extracted from the input lines. Each license type is denoted by a line that starts with "//" followed by the license type. The function should stop processing input lines when it encounters a line containing only the word "END".
"""

def extract_license_types(input_lines):
    license_types = []
    for line in input_lines:
        if line.strip() == "END":
            break
        if line.startswith("//"):
            license_type = line[2:].strip()
            license_types.append(license_type)
    return license_types