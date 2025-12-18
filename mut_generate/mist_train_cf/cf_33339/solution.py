"""
QUESTION:
Write a Python function called `organize_imports` that takes a list of module imports as input, where each import is a string with dot-separated segments, and returns a hierarchical representation of the imports as a dictionary. The keys of the dictionary should be the top-level segments of the import paths, and the values should be dictionaries representing the next level of the hierarchy. If a segment has no sub-segments, its value should be an empty dictionary.
"""

def organize_imports(imports):
    hierarchy = {}
    for imp in imports:
        segments = imp.split('.')
        current_level = hierarchy
        for segment in segments:
            if segment not in current_level:
                current_level[segment] = {}
            current_level = current_level[segment]
    return hierarchy