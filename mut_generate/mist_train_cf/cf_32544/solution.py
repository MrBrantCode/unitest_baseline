"""
QUESTION:
Implement a function `extract_urls` that takes a string containing the content of a Django URL configuration file and returns a list of URLs mapped to views. The URL configuration file follows the standard Django format, where URLs are mapped to views using the `urlpatterns` list. The function should handle variations in URL mapping syntax and only extract the URLs. 

The input string contains the content of the Django URL configuration file, and the output is a list of URLs mapped to views. The function should extract the URLs from the given string.
"""

from typing import List
import re

def extract_urls(url_config: str) -> List[str]:
    urls = re.findall(r"path\(['\"](.*?)['\"].*?\)", url_config)
    return urls