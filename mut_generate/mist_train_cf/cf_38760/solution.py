"""
QUESTION:
Create a function `parse_language_classifiers` that takes a list of strings representing programming language classifiers in the format `'Programming Language :: LanguageName :: Version'` (where the version part is optional) and returns a dictionary where the keys are the unique programming languages and the values are dictionaries containing the count of each version for that language.
"""

from typing import List, Dict

def parse_language_classifiers(classifiers: List[str]) -> Dict[str, Dict[str, int]]:
    language_versions = {}
    for classifier in classifiers:
        parts = classifier.split(' :: ')
        language = parts[1]
        version = parts[2] if len(parts) > 2 else None
        if language not in language_versions:
            language_versions[language] = {}
        if version not in language_versions[language]:
            language_versions[language][version] = 1
        else:
            language_versions[language][version] += 1
    return language_versions