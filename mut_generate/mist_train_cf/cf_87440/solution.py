"""
QUESTION:
Create a function `organize_pet_owners` that takes a list of strings, where each string represents a pet owner's information in the format "Owner: pet1_count pet1_type, pet2_count pet2_type, ...". The function should return a dictionary where the keys are the owner's names and the values are lists of tuples containing the pet type and count. The function should be able to handle incorrect pet information and ignore it.
"""

import re

def organize_pet_owners(pet_info_list):
    pet_owners = {}
    
    for pet in pet_info_list:
        # Extract the owner's name
        match = re.match(r"([A-Za-z]+):", pet)
        if match:
            owner = match.group(1)
            pet_info = re.findall(r"(\d+)\s+([A-Za-z]+)", pet)
            if pet_info:
                pet_owners[owner] = [(int(count), animal) for count, animal in pet_info]
                
    return pet_owners