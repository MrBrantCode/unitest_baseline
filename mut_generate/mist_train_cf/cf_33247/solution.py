"""
QUESTION:
Create a function named `analyze_trainer_description` that takes a string representing a localized description of a technology trainer as input. The string starts with the phrase "Looks up a localized string similar to" followed by the trainer's details, which includes their experience, skills, and areas of expertise, and ends with a period. The function should extract the trainer's name (the first word after the phrase "Looks up a localized string similar to"), count the occurrences of the word "programowanie" (programming) in the description, and replace all occurrences of the word "technologii" (technology) with "inżynierii" (engineering) in the description. The function should return the extracted name, the count of occurrences of "programowanie", and the modified description.
"""

import re

def analyze_trainer_description(description):
    name_match = re.search(r"Looks up a localized string similar to (\w+)", description)
    name = name_match.group(1) if name_match else "Unknown"

    occurrences_programowanie = description.count("programowanie")

    modified_description = description.replace("technologii", "inżynierii")

    return name, occurrences_programowanie, modified_description