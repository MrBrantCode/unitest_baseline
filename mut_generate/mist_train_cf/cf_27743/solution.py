"""
QUESTION:
Create a function named `extract_bash_script_info` that takes a Bash script as input. The function should extract the following information from the script: 
- The name of the repository (reponame)
- The name of the file being processed (filename)
- The copyright holder of the script

Assume the repository name and file name are enclosed within angle brackets `<>` and the copyright holder is specified in a line starting with "Copyright". The function should return the extracted information in a structured format, such as a dictionary.
"""

import re

def extract_bash_script_info(script):
    info = {
        "reponame": "",
        "filename": "",
        "copyright": ""
    }

    # Extract reponame and filename
    repo_filename_match = re.search(r'<(.*?)>(.*?)<(.*)>', script)
    if repo_filename_match:
        info["reponame"] = repo_filename_match.group(1)
        info["filename"] = repo_filename_match.group(2) + repo_filename_match.group(3)

    # Extract copyright
    copyright_match = re.search(r'Copyright\s+(.*)\.', script)
    if copyright_match:
        info["copyright"] = copyright_match.group(1)

    return info