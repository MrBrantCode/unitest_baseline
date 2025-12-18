"""
QUESTION:
Create a function named `parse_urls` that takes a list of URLs and a dictionary of SHA256 hashes as input, and returns a dictionary where the keys are the package names and the values are tuples containing the version and SHA256 hash. The URLs are in the format "https://<domain>/src/contrib/<package_name>_<version>.tar.gz". If a version is not found in the SHA256 hashes dictionary, it should not be included in the output.
"""

from typing import List, Dict, Tuple

def parse_urls(urls: List[str], sha256_hashes: Dict[str, str]) -> Dict[str, Tuple[str, str]]:
    parsed_data = {}
    for url in urls:
        parts = url.split('/')
        package_info = parts[-1].split('_')
        package_name = package_info[0]
        version = package_info[1].replace('.tar.gz', '')
        if version in sha256_hashes:
            parsed_data[package_name] = (version, sha256_hashes[version])
    return parsed_data