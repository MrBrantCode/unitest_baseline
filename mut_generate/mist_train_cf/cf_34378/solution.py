"""
QUESTION:
Generate a list of download links for a specified repository and commit, with each link pointing to a file with one of the specified extensions.

The function, `generate_download_links`, should take in three parameters: `repository` (str), `commit` (str), and `file_extensions` (List[str]), and return a list of download links (List[str]). 

The base download link should be in the format "https://bitbucket.org/{repository}/get/{commit}.tar.gz", and for specific extensions, the link should be in the format "{base_link}?file=*.extension".
"""

from typing import List

def generate_download_links(repository: str, commit: str, file_extensions: List[str]) -> List[str]:
    base_link = f"https://bitbucket.org/{repository}/get/{commit}.tar.gz"
    download_links = [base_link]

    for extension in file_extensions:
        download_links.append(f"{base_link}?file=*.{extension}")

    return download_links