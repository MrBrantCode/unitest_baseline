"""
QUESTION:
Create a function called `parse_pet_owners` that takes a list of strings as input where each string represents a pet owner and their pets. The string format is "Owner's Name: number of pet1 type1, number of pet2 type2, ...". The function should return a dictionary where the keys are the owner's names and the values are lists of tuples, each containing the type of pet and the number of pets owned. The function should be able to handle strings with any number of pet types and should ignore any strings that do not match the expected format.
"""

import re

def parse_pet_owners(pets):
    pet_owners = {}
    for pet in pets:
        # Extract the owner's name
        match = re.match(r"([A-Za-z]+):", pet)
        if match:
            owner = match.group(1)
            pet_info = re.findall(r"(\d+)\s+([A-Za-z]+)", pet)
            if pet_info:
                pet_owners[owner] = [(int(count), animal) for count, animal in pet_info]
    return pet_owners