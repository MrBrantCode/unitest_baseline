"""
QUESTION:
Write a function `extract_package_info` that takes a string `long_description` as input and returns a dictionary containing the extracted information. The dictionary should have the following keys: 'name', 'version', 'author', 'author_email', and 'description'. The values associated with these keys should be the corresponding extracted information from the `long_description`. 

The `long_description` string is expected to contain the package information in the following format:
```
setup(name='package_name',
      version=version_number,
      author='author_name',
      author_email='author_email',
      description='package_description'
)
```
The function should extract the package name, version number, author's name, author's email, and package description from the `long_description` string and store them in the dictionary.
"""

import re

def extract_package_info(long_description):
    info = {}
    info['name'] = re.search(r"setup\(name='(.*?)',", long_description).group(1)
    info['version'] = float(re.search(r"version=(.*?),", long_description).group(1))
    info['author'] = re.search(r"author='(.*?)',", long_description).group(1)
    info['author_email'] = re.search(r"author_email='(.*?)',", long_description).group(1)
    info['description'] = re.search(r"description='(.*?)'", long_description).group(1)
    return info