"""
QUESTION:
Implement a function `process_rules(rules)` that takes a list of rules as input, where each rule is a dictionary with keys 'name', 'condition', and 'action', representing a rule's name, a boolean condition, and an action to be taken if the condition is met, respectively. The function should return a list of modified actions by removing any rules where the condition is False and appending the rule's name to the 'action' string for the remaining rules.
"""

from typing import List, Dict, Union

def process_rules(rules: List[Dict[str, Union[str, bool]]]) -> List[str]:
    return [rule['action'] + '_' + rule['name'] for rule in rules if rule['condition']]