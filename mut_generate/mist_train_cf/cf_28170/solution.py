"""
QUESTION:
Write a function `find_invalid_values(rules, nearby_tickets)` that takes a dictionary `rules` where each key corresponds to a list of valid ranges and a list `nearby_tickets` of tickets, where each ticket is a list of integers. The function should return the sum of all invalid values in the nearby tickets. A value is considered invalid if it does not satisfy any of the valid ranges in the rules.
"""

def find_invalid_values(rules, nearby_tickets):
    invalid_values = []
    for ticket in nearby_tickets:
        for value in ticket:
            valid = False
            for rule_ranges in rules.values():
                for r in rule_ranges:
                    if r[0] <= value <= r[1]:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                invalid_values.append(value)
    return sum(invalid_values)