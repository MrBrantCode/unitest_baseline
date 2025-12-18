"""
QUESTION:
Create a function `find_acronym(acronym)` that takes an acronym as input and returns its full form. The function should be case insensitive and use a predefined dictionary with at least ten acronym-full form pairs. If the acronym is not found in the dictionary, the function should return a message indicating that it's not in the predefined list. The function should not include the dynamic search portion for this problem.
"""

acronym_dict = {
    "GDP": "Gross Domestic Product",
    "FBI": "Federal Bureau of Investigation",
    "BBC": "British Broadcasting Corporation", 
    "NASA": "National Aeronautics and Space Administration",
    "NATO": "North Atlantic Treaty Organization",
    "WHO": "World Health Organization",
    "UN": "United Nations",
    "USA": "United States of America",
    "UK": "United Kingdom",
    "EU": "European Union",
}

def entrance(acronym):
    acronym = acronym.upper()
    if acronym in acronym_dict:
        return acronym_dict[acronym]
    else:
        # In real application, the dynamic search part will be placed here. 
        return "Acronym not found in predefined list"