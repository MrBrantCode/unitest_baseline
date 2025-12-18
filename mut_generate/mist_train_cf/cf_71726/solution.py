"""
QUESTION:
Implement a function `group_with_rule(numbers, rule)` that groups the elements of the input list `numbers` based on the output of the arithmetical rule defined by the string `rule`. The function should return the groups in the order in which their elements first appear in the original list. The input list `numbers` contains integers, and the input string `rule` represents a valid Python expression that takes a single number `n` as input.
"""

def group_with_rule(numbers, rule):
    rule_func = eval('lambda n: ' + rule)
    groups = {}
    result = []

    for n in numbers:
        key = rule_func(n)
        if key not in groups:
            groups[key] = []
            result.append(groups[key])
        groups[key].append(n)

    return result