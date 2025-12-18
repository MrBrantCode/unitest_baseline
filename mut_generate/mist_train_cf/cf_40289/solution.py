"""
QUESTION:
Write a function `custom_skill_sort(skills)` that takes a list of dictionaries representing skills with 'name' and 'level' keys, and returns the sorted list in ascending order by 'name' (case-insensitive) and then by 'level' in the order: 'Beginner' < 'Intermediate' < 'Advanced'.
"""

def custom_skill_sort(skills):
    def custom_sort_key(skill):
        return skill['name'].lower(), {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}[skill['level']]

    return sorted(skills, key=custom_sort_key)