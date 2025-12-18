"""
QUESTION:
Create a function `extract_repo_info(metadata: str) -> dict` that takes in a string `metadata` and returns a dictionary containing two keys: 'stars' and 'version'. The 'stars' key should contain the non-negative integer value following '<gh_stars>' in a line, and the 'version' key should contain the string value on the line immediately following 'from ._version import __version__' in the input string.
"""

def extract_repo_info(metadata: str) -> dict:
    repo_info = {'stars': 0, 'version': ''}
    lines = metadata.split('\n')
    for i in range(len(lines)):
        if lines[i].startswith('<gh_stars>'):
            repo_info['stars'] = int(lines[i].split('<gh_stars>')[1])
        elif lines[i] == 'from ._version import __version__':
            repo_info['version'] = lines[i+1]
    return repo_info