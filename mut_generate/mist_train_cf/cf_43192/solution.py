"""
QUESTION:
Implement a function named `process` that takes a list of code snippets as strings and returns a list of dictionaries containing information about each code snippet. Each dictionary should have the following keys: "snippet" (the original code snippet), "keyword_counts" (a dictionary with keyword counts), "has_loops" (a boolean indicating the presence of loop constructs), "has_conditionals" (a boolean indicating the presence of conditional constructs), and "variable_assignments" (a list of variable assignments). The function should count occurrences of keywords "if", "else", "for", "while", "def", and "return", and identify variable assignments as lines containing the "=" operator.
"""

from typing import List, Dict, Union

def process(code: List[str]) -> List[Dict[str, Union[str, int]]]:
    keyword_list = ["if", "else", "for", "while", "def", "return", "in"]
    output = []
    
    for snippet in code:
        snippet_info = {
            "snippet": snippet,
            "keyword_counts": {keyword: snippet.count(keyword) for keyword in keyword_list},
            "has_loops": any(keyword in snippet for keyword in ["for", "while"]),
            "has_conditionals": any(keyword in snippet for keyword in ["if", "else"]),
            "variable_assignments": [line.strip() for line in snippet.split("\n") if "=" in line]
        }
        output.append(snippet_info)
    
    return output