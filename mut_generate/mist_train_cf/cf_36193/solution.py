"""
QUESTION:
Write a function `extract_disclaimer(licenses)` that takes a list of strings representing software licenses as input. Extract the disclaimer text from each license, defined as the portion of the license before the first occurrence of the word "LIMITED" in all capital letters, and return a list of strings containing the extracted disclaimer texts.
"""

from typing import List

def extract_disclaimer(licenses: List[str]) -> List[str]:
    disclaimers = []
    for license in licenses:
        disclaimer = ""
        index = license.find("LIMITED")
        if index != -1:
            disclaimer = license[:index]
        disclaimers.append(disclaimer)
    return disclaimers