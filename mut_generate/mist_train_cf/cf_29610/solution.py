"""
QUESTION:
Implement a Python function `extract_info` that takes a code snippet as input and returns a dictionary containing the extracted information. The function should extract the name of the resource being initialized in the constructor and the version number mentioned in the comments. If the version number is not found in the comments, the dictionary should contain "Version" with a value of "Not specified". The code snippet contains a class constructor with parameters and comments.
"""

import re

def extract_info(code_snippet):
    info_dict = {}
    
    # Extract resource name
    resource_name_match = re.search(r'resource_name:\s*(\w+)', code_snippet)
    if resource_name_match:
        info_dict["ResourceName"] = resource_name_match.group(1)
    
    # Extract version from comments
    version_match = re.search(r'Release\s+(\d+\.\d+\.\d+)', code_snippet)
    if version_match:
        info_dict["Version"] = version_match.group(1)
    else:
        info_dict["Version"] = "Not specified"
    
    return info_dict