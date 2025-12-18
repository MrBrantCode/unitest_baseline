"""
QUESTION:
Design a function `identify_language(file_path)` that identifies the programming language used in a given file based on its extension. The function should support the following languages and file extensions: HTML (.html), CSS (.css), JavaScript (.js), PHP (.php), and SQL (.sql). If the file extension is not supported, the function should return "Unknown language".
"""

import os

def identify_language(file_path):
    _, ext = os.path.splitext(file_path)
    supported_languages = {
        ".html": "HTML",
        ".css": "CSS",
        ".js": "JavaScript",
        ".php": "PHP",
        ".sql": "SQL"
    }
    return supported_languages.get(ext, "Unknown language")