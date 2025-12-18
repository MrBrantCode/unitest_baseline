"""
QUESTION:
Implement a function `organize_test_cases(test_cases)` that takes a list of strings representing test cases in the format "category.test" and returns a nested dictionary representing the hierarchical structure of the test cases. The keys in the dictionary represent the categories, and the values are either nested dictionaries (if there are subcategories) or an empty dictionary (if there are no subcategories).
"""

def organize_test_cases(test_cases):
    test_structure = {}
    for test_case in test_cases:
        categories = test_case.split('.')
        current_level = test_structure
        for category in categories:
            if category not in current_level:
                current_level[category] = {}
            current_level = current_level[category]
    return test_structure