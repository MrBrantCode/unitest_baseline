"""
QUESTION:
Write a function `find_unique_languages` that takes a list of language assignments as input, where each assignment is a string in the format "language = (script)". The function should return the number of unique languages and a list of languages with circular dependencies. 

A circular dependency exists when a language is mapped to itself, either directly or indirectly. The script can be another language or "None", indicating that the language is not mapped to any other language.
"""

def find_unique_languages(assignments):
    unique_languages = set()
    dependencies = {}
    for assignment in assignments:
        language, script = assignment.split(' = ')
        language = language.strip()
        script = script.strip('()')
        if script != 'None':
            dependencies[language] = script
        unique_languages.add(language)

    circular_dependencies = set()
    for language in dependencies:
        visited = set()
        current = language
        while current in dependencies and current not in visited:
            visited.add(current)
            current = dependencies[current]
        if current in visited:
            circular_dependencies.add(current)

    num_unique_languages = len(unique_languages)
    return num_unique_languages, list(circular_dependencies)