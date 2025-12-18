"""
QUESTION:
Implement a function `analyze_metadata(dataset: List[str]) -> Dict[str, Dict[str, int]]` that takes a list of strings representing software package metadata as input, where each string is in the format "Category :: Value". The function should return a dictionary where the keys are programming languages and the values are dictionaries containing the count of each operating system used with that programming language. If a package does not specify a programming language, it should be categorized under an empty string key.
"""

from typing import List, Dict

def entrance(dataset: List[str]) -> Dict[str, Dict[str, int]]:
    language_os_distribution = {}
    
    language = ""
    
    for data in dataset:
        parts = data.split(" :: ")
        if len(parts) == 2:
            category, value = parts
            if category == "Programming Language":
                language = value
                if language not in language_os_distribution:
                    language_os_distribution[language] = {}
            elif category == "Operating System":
                if language not in language_os_distribution:
                    language_os_distribution[language] = {}
                if value not in language_os_distribution[language]:
                    language_os_distribution[language][value] = 1
                else:
                    language_os_distribution[language][value] += 1
    
    return language_os_distribution