"""
QUESTION:
Create a function called `parse_classifiers` that takes a list of classifiers as input, where each classifier is a string in the format "Category :: Value", and returns a dictionary containing the classification categories as keys and their corresponding values. The function should handle cases where the category or value contains special characters or spaces.
"""

def parse_classifiers(classifiers):
    parsed_dict = {}
    for classifier in classifiers:
        category, value = classifier.split(" :: ")
        parsed_dict[category] = value
    return parsed_dict