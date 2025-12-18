"""
QUESTION:
Write a function `process_files(INPUT_PATH)` that takes a string `INPUT_PATH` representing the path to the directory containing files with names in the pattern `<name>-<number>-<number>-<number>.<extension>`. The function should calculate `cellX` by subtracting 90 from the second number, `cellY` by subtracting 40 from the third number, and store the `zoom` value as the fourth number. Return a list of tuples containing the calculated `cellX`, `cellY`, and `zoom` values for each file in the directory.
"""

import os
import re

def entance(INPUT_PATH):
    result = []
    for filename in os.listdir(INPUT_PATH):
        matchResult = re.search('([a-zA-Z]+)-([0-9]+)-([0-9]+)-([0-9]+)\.', filename)
        if (not matchResult): continue

        cellX = int(matchResult.group(2)) - 90
        cellY = int(matchResult.group(3)) - 40
        zoom = matchResult.group(4)
        
        result.append((cellX, cellY, zoom))
    
    return result