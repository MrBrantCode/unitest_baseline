"""
QUESTION:
Write a function `extract_years` that takes a string `copyright_notice` as input and returns a list of strings representing the years mentioned in the copyright notice. The input string is a Python code snippet containing the copyright notice, with a length between 1 and 1000 characters. The function should extract all 4-digit numbers from the input string, assuming they represent years.
"""

from typing import List
import re

def extract_years(copyright_notice: str) -> List[str]:
    years = re.findall(r'\b\d{4}\b', copyright_notice)
    return years