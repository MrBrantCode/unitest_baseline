"""
QUESTION:
Create a function `extractCopyrightYears` that takes a string `codeSnippet` as input and returns a sorted list of unique copyright years found in the snippet. The input code snippet is a comment block that contains copyright information in the format "Copyright (c) year1, year2, year3, ...". The years will be comma-separated and may appear in any order within the comment block. The years may not be consecutive.
"""

from typing import List

def extractCopyrightYears(codeSnippet: str) -> List[int]:
    start_index = codeSnippet.find("Copyright (c)") + len("Copyright (c)")
    end_index = codeSnippet.find("Sakai Foundation")
    years_str = codeSnippet[start_index:end_index].strip().replace(",", "")
    years = [int(year) for year in years_str.split() if year.isdigit()]
    return sorted(list(set(years)))