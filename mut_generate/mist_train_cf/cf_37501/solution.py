"""
QUESTION:
Write a function `generateCommandLine(options: List[Tuple[str, str]]) -> str` that takes a list of tuples representing server configuration options and returns a command-line string constructed based on the format: "-Dplay.server.https.key=value" for each option, separated by a space.
"""

from typing import List, Tuple

def generateCommandLine(options: List[Tuple[str, str]]) -> str:
    return " ".join(f"-Dplay.server.https.{key}={value}" for key, value in options)