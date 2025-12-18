"""
QUESTION:
Implement a function `parse_module_docstring(docstring: str) -> Tuple[str, str]` that takes a module docstring in reStructuredText format and returns a tuple containing the platform and synopsis information. The platform and synopsis sections are always present in the docstring, preceded by the `:platform:` and `:synopsis:` directives, respectively.
"""

from typing import Tuple

def entrance(docstring: str) -> Tuple[str, str]:
    platform_start = docstring.find(":platform:")
    platform_end = docstring.find(":synopsis:")
    platform = docstring[platform_start + 10:platform_end].strip()

    synopsis_start = docstring.find(":synopsis:")
    synopsis = docstring[synopsis_start + 10:].strip()

    return platform, synopsis