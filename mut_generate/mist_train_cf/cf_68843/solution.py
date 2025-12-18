"""
QUESTION:
Write a function `classify_object(object_name, categories)` that classifies an object's name into proper categories based on the given set of categories. The function should be case-insensitive and handle cases where the object's name is not found in any category and cases where the object's name is found in multiple categories. The function should return a string indicating the category or categories the object belongs to.
"""

def classify_object(object_name, categories):
    object_name = object_name.lower()
    found_categories = []

    for category, objects in categories.items():
        if object_name in (object.lower() for object in objects):
            found_categories.append(category)

    if not found_categories:
        return f"'{object_name}' is not found in any categories."
    elif len(found_categories) > 1:
        return f"'{object_name}' is found in multiple categories: {', '.join(found_categories)}"
    else:
        return f"'{object_name}' belongs to '{found_categories[0]}' category."