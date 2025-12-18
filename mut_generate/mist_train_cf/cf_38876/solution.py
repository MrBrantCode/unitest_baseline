"""
QUESTION:
Create a function `gitDiff` that takes two string parameters: `workingDirectory` and `stagingArea`. The function should return a string representing the difference between the two input strings, defined as the set of characters that need to be added to the working directory to make it identical to the staging area. If a character is present in the staging area but not in the working directory, it should be included in the difference string. If a character is present in both strings, it should not be included in the difference string.
"""

def gitDiff(workingDirectory, stagingArea):
    difference = ""
    for char in stagingArea:
        if char not in workingDirectory:
            difference += char
    return difference