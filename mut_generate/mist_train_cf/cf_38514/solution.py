"""
QUESTION:
Create a function `apply_substitution_rules` that takes a source string and a list of substitution rules as input. The substitution rules are in the format `s/FIND/REPLACE/g` where `FIND` is the string to be found in the source string and `REPLACE` is the string to replace `FIND` with. The function should apply the rules to the source string and return the final result.
"""

import re

def apply_substitution_rules(source, rules):
    result = source
    for rule in rules:
        pattern = rule.split('/')[1]  # Extract the pattern to find
        replacement = rule.split('/')[2]  # Extract the replacement string
        result = re.sub(pattern, replacement, result)  # Apply the substitution
    return result