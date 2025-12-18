"""
QUESTION:
Given a version history log as a multi-line string and a target version number as a string, write a function `extract_breaking_changes(version_history, target_version)` that returns a list of breaking changes for the target version. The version history log has each line representing a version and its associated breaking changes, with breaking changes denoted by lines starting with "###" followed by the version number and the word "breaking changes".
"""

def extract_breaking_changes(version_history, target_version):
    breaking_changes = []
    lines = version_history.split('\n')
    version_found = False
    for line in lines:
        if line.startswith("### " + target_version + " breaking changes"):
            version_found = True
        elif line.startswith("### ") and version_found:
            break
        elif version_found and line.strip() != "":
            breaking_changes.append(line.strip('- '))
    return breaking_changes