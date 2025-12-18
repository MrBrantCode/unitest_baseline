"""
QUESTION:
Write a function named `count_function_calls` that takes a list of strings `snippets` as input, where each string represents a code snippet. The function should count the occurrences of the specific function call `result.assert_installed('project', editable=False)` within the snippets, regardless of indentation or spacing, and return the total count as an integer. The function call will always be in the specified format.
"""

from typing import List
import re

def count_function_calls(snippets: List[str]) -> int:
    function_call = "result.assert_installed('project', editable=False)"
    count = 0
    for snippet in snippets:
        count += len(re.findall(re.escape(function_call), snippet))
    return count