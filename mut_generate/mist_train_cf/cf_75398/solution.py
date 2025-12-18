"""
QUESTION:
Create a function called `categorize_denominations` that takes two parameters: a list of known entries for each category (fruits, animals, programming languages) and a list of mixed denominations. The function should return three separate lists, each containing the corresponding denominations sorted alphabetically. The known entries for each category are assumed to be known beforehand.
"""

def categorize_denominations(known_entries, mixed_denominations):
    """
    Categorize mixed denominations into their respective categories.

    Args:
    known_entries (dict): A dictionary with category names as keys and lists of known entries as values.
    mixed_denominations (list): A list of mixed denominations.

    Returns:
    dict: A dictionary with category names as keys and sorted lists of corresponding denominations as values.
    """
    categorized = {category: [] for category in known_entries.keys()}
    
    # iterate through each item in the input list
    for item in mixed_denominations:
        # identify the category of the item and add it to the corresponding list
        for category, known_items in known_entries.items():
            if item in known_items:
                categorized[category].append(item)

    # sort each list
    for category in categorized.keys():
        categorized[category].sort()

    return categorized