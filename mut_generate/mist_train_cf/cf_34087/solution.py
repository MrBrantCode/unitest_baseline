"""
QUESTION:
Write a function named `extract_rules` that takes a string `text` as input, where `text` contains a series of rules and guidelines for a system, each rule numbered and followed by a statement. The function should return a list of tuples, where each tuple contains the rule number and the corresponding statement. The input `text` is a string containing the rules and statements, separated by "<br/>".
"""

def extract_rules(text):
    rules = []
    lines = text.split("<br/>")  
    for line in lines:
        parts = line.split(".")  
        if len(parts) > 1:
            rule_number = int(parts[0])  
            statement = ".".join(parts[1:]).strip()  
            rules.append((rule_number, statement))  
    return rules