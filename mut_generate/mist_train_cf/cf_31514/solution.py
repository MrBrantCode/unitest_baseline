"""
QUESTION:
Implement a function `extract_information(output: str) -> dict` that takes a multi-line string as input, where each line represents a separate piece of information in the format 'key: value'. The function should extract the value from the first three lines and return a dictionary containing the extracted information. The first line is expected to contain the name, the second line the version, and the third line the date of the last update. The function should assume that the input string will always have at least three lines and the format of the output will adhere to the described structure.
"""

def extract_information(output: str) -> dict:
    lines = output.strip().split('\n')
    return {
        "name": lines[0].split(': ')[1],
        "version": lines[1].split(': ')[1],
        "last_update": lines[2].split(': ')[1]
    }