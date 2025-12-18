"""
QUESTION:
Implement the `sort_fields` function, which takes as input a list of rules and a list of nearby tickets. Each rule is a tuple containing a field name and a list of valid value ranges, and each ticket is a list of field values. The function should return the correct order of field names based on the given rules and tickets. The function should be able to handle any number of fields and tickets.
"""

def sort_fields(rules, nearby_tickets):
    def is_valid_value(value, rule):
        for r in rule:
            if r[0] <= value <= r[1]:
                return True
        return False

    valid_tickets = [ticket for ticket in nearby_tickets if all(any(is_valid_value(value, rule[1]) for rule in rules) for value in ticket)]
    possible_idxs_per_field = {field: set(range(len(rules))) for field in range(len(rules))}
    
    for ticket in valid_tickets:
        for idx, value in enumerate(ticket):
            for field, rule in enumerate(rules):
                if not is_valid_value(value, rule[1]):
                    possible_idxs_per_field[field].discard(idx)
    
    fields = [None] * len(rules)
    while any(len(possible_idxs_per_field[field]) > 0 for field in possible_idxs_per_field):
        for field, possible_idxs in possible_idxs_per_field.items():
            if len(possible_idxs) == 1:
                idx = possible_idxs.pop()
                fields[field] = idx
                for other_idxs in possible_idxs_per_field.values():
                    other_idxs.discard(idx)
    
    return [rules[field][0] for field, idx in sorted(enumerate(fields), key=lambda x: x[1])]