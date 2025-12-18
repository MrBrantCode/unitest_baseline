"""
QUESTION:
Write a function named `extract_repo_info` that takes a code snippet as input and extracts the range of stars, repository name, and version. The code snippet is in the format:
```
<gh_stars>1-10
    /*==============================
    RepositoryName vVersion
```
The function should return a tuple containing the range of stars, repository name, and version. The repository name is the word preceding 'v' and the version starts with 'v' followed by a number. The range of stars is the number after '<gh_stars>'.
"""

import re

def extract_repo_info(code_snippet):
    # Extracting the range of stars
    stars_range = re.search(r'<gh_stars>(\d+-\d+)', code_snippet).group(1)
    
    # Extracting the repository name and version
    repo_info = re.search(r'(?<=\n\s{4})(\w+)\s(v\d+\.\d+\.\d+)', code_snippet).groups()
    
    return stars_range, repo_info[0], repo_info[1]