"""
QUESTION:
Create a function named `parse_rules` that takes a string `code_snippet` as input and returns a dictionary where the keys are the rule types ("general_rules" and "utility_rules") and the values are lists of rules belonging to each type. The rules in the `code_snippet` are prefixed with '*' for general rules and '#' for utility rules. The function should extract the rules from the `code_snippet` based on their prefixes and return the dictionary.
"""

def parse_rules(code_snippet: str) -> dict:
    rules_dict = {"general_rules": [], "utility_rules": []}
    lines = code_snippet.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("*"):
            rules_dict["general_rules"].append(line.lstrip("*").strip(","))
        elif line.startswith("#"):
            rules_dict["utility_rules"].append(line.lstrip("#").strip())
    return rules_dict