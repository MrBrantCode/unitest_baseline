"""
QUESTION:
Implement a function `evaluate_rules` to match antecedents with consequents in a rule-based system. The function should support millions of operations per rule and handle repeated operators across rules. Consider using alternative pattern matching algorithms to the RETE algorithm, such as the Leaps Algorithm, TREAT Algorithm, or Backward Chaining, to optimize memory usage and performance.
"""

def evaluate_rules(rules, facts):
    """
    Evaluate a set of rules against a set of facts.

    This is a basic implementation of a rule-based system using the Backward Chaining algorithm.

    Args:
        rules (list): A list of rules, where each rule is a dictionary with 'antecedents' and 'consequent' keys.
        facts (list): A list of facts, where each fact is a string.

    Returns:
        list: A list of consequents that are true based on the given facts and rules.
    """

    def backward_chaining(consequent, facts, rules):
        """
        Apply the Backward Chaining algorithm to find the antecedents of a consequent.

        Args:
            consequent (str): The consequent to find antecedents for.
            facts (list): A list of facts.
            rules (list): A list of rules.

        Returns:
            bool: True if the consequent is true, False otherwise.
        """

        # Check if the consequent is a fact
        if consequent in facts:
            return True

        # Find rules with the consequent
        applicable_rules = [rule for rule in rules if rule['consequent'] == consequent]

        # If no rules are found, the consequent is not true
        if not applicable_rules:
            return False

        # Apply the antecedents of the applicable rules
        for rule in applicable_rules:
            if all(backward_chaining(antecedent, facts, rules) for antecedent in rule['antecedents']):
                return True

        # If no antecedents are true, the consequent is not true
        return False

    # Evaluate each rule
    true_consequents = []
    for rule in rules:
        if backward_chaining(rule['consequent'], facts, rules):
            true_consequents.append(rule['consequent'])

    return true_consequents