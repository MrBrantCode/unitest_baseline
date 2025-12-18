"""
QUESTION:
Implement a function `validateFileNames` that takes a list of file names as input and returns a list of boolean values indicating whether each file name is valid or not. A valid file name does not contain any special characters (`!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `-`, `+`, `=`, `[`, `]`, `{`, `}`, `|`, `\`, `;`, `:`, `'`, `"`, `,`, `.`, `<`, `>`, `/`, `?`, or `~`), does not start or end with a space, and does not contain consecutive spaces.
"""

from typing import List

def validateFileNames(fileNames: List[str]) -> List[bool]:
    def is_valid_file_name(name: str) -> bool:
        if any(char in name for char in "!@#$%^&*()-+=[]{}|\\;:'\",<>/?.~"):
            return False
        if name.startswith(" ") or name.endswith(" "):
            return False
        if "  " in name:
            return False
        return True

    return [is_valid_file_name(name) for name in fileNames]