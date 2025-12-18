"""
QUESTION:
Implement the function `update_language_mapping(mapping, common_languages, verbose)` that updates a dictionary mapping file extensions to programming languages based on the following conditions:

- If the language for a given extension is already in the common languages list, update the mapping.
- If the language for a given extension is not in the common languages list, but a new language is provided and is in the common languages list, update the mapping.
- If neither the old nor the new language is in the common languages list, apply the first-come-first-served principle, blocking the old language and updating the mapping.
- If none of the above conditions are met, do not update the mapping.

The function takes in three parameters: 
- `mapping`: a dictionary mapping file extensions to programming languages.
- `common_languages`: a list of common programming languages.
- `verbose`: a boolean flag indicating whether to print messages during the update process.

The function should return the updated mapping.
"""

def update_language_mapping(mapping: dict, common_languages: list, verbose: bool) -> dict:
    updated_mapping = mapping.copy()
    for extension, new_language in mapping.items():
        old_language = updated_mapping[extension]
        if old_language in common_languages:
            if verbose:
                print(f"{extension}: UPDATE {old_language} -> {old_language} (Common)")
        elif new_language in common_languages:
            updated_mapping[extension] = new_language
            if verbose:
                print(f"{extension}: UPDATE {old_language} -> {new_language} (Common)")
        elif old_language not in common_languages and new_language not in common_languages:
            if verbose:
                print(f"{extension}: BLOCK  {old_language} (First) | {new_language}")
        return updated_mapping