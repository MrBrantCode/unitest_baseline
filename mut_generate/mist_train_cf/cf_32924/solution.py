"""
QUESTION:
Write a function `extract_info_from_code` that takes a string `code_snippet` as input and returns a dictionary containing the repository name, file path, and authors' information. 

The input `code_snippet` is a string that contains the repository name, file path, and authors' information in the following format: `<reponame>repository_name<filename>file_path...# Authors: author_name <author_email>`. 

The output dictionary should have the following keys: `repository_name`, `file_path`, and `authors`. The `authors` key should have a list of dictionaries as its value, where each dictionary contains the `name` and `email` of an author. 

Note that the input string may contain multiple authors.
"""

import re

def extract_info_from_code(code_snippet):
    info_dict = {}
    
    # Extract repository name and file path using regular expressions
    match = re.search(r'<reponame>(.*?)<filename>(.*?)\n', code_snippet)
    if match:
        info_dict['repository_name'] = match.group(1)
        info_dict['file_path'] = match.group(2)
    
    # Extract authors using regular expressions
    authors = re.findall(r'Authors: (.*?) <(.*?)>', code_snippet)
    info_dict['authors'] = [{'name': author[0], 'email': author[1]} for author in authors]
    
    return info_dict