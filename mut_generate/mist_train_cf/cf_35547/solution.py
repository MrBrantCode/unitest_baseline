"""
QUESTION:
Create a function `process_libraries` that takes two parameters: `languages` and `libraries`, both of which are lists of strings representing programming languages and their associated libraries, respectively. Each string in both lists is a non-empty string containing only alphanumeric characters and can be in lowercase or uppercase. The function should return a list of strings representing the actions to be performed based on the presence of specific languages and libraries. If a language is present without an associated library, the action should be "Install {language} compiler". If a language is present with an associated library, the action should be "Compile {language} program using {library}".
"""

def process_libraries(languages: list, libraries: list) -> list:
    actions = []
    language_library_map = dict(zip(languages, libraries))

    for language in languages:
        if language in language_library_map:
            library = language_library_map[language]
            actions.append(f'Compile {language} program using {library}')
        else:
            actions.append(f'Install {language} compiler')

    return actions