"""
QUESTION:
Implement a function named `snake_to_kebab` that takes a string in snake_case format as input and returns the equivalent string in kebab-case format. The function should replace all underscores (_) with hyphens (-).
"""

def snake_to_kebab(snake_case_string):
    kebab_case_string = snake_case_string.replace('_', '-')
    return kebab_case_string