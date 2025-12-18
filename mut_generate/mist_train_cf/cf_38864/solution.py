"""
QUESTION:
Create a function `extract_citation_info` that takes a string `bibliography` as input. The input string contains one or more citations, each enclosed within a pair of triple double quotes (`"""`) and may span multiple lines. The function should extract the authors' names, publication year, title, and journal name from each citation and return a list of dictionaries, where each dictionary has the keys "authors", "year", "title", and "journal" corresponding to the extracted information.
"""

import re

def extract_citation_info(bibliography):
    citations = re.findall(r'"""(.*?)"""', bibliography, re.DOTALL)
    extracted_info = []
    for citation in citations:
        info = {}
        lines = citation.strip().split('\n')
        authors_year = lines[0].strip().split('.')
        info["authors"] = authors_year[0].strip()
        info["year"] = authors_year[1].strip()
        title_journal = lines[1].strip().split('.')
        info["title"] = title_journal[0].strip()
        info["journal"] = title_journal[1].strip()
        extracted_info.append(info)
    return extracted_info