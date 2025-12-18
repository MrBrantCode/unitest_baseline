"""
QUESTION:
Create a function `docker_registry` that takes in two parameters: a list of Docker image names and a list of commands. The function should execute the commands on the images and return a list of results. Each command can be either "push" to add an image to the registry or "pull" to retrieve an image from the registry. The function should return "Image not found" if a "pull" command is issued for an image not in the registry, "Image already exists" if a "push" command is issued for an existing image, "Image pushed" if a new image is added to the registry, and "Image pulled" if an existing image is retrieved.
"""

from typing import List

def docker_registry(images: List[str], commands: List[str]) -> List[str]:
    registry = set(images)
    result = []
    
    for command in commands:
        action, image = command.split()
        if action == "push":
            if image in registry:
                result.append("Image already exists")
            else:
                registry.add(image)
                result.append("Image pushed")
        elif action == "pull":
            if image in registry:
                result.append("Image pulled")
            else:
                result.append("Image not found")
    
    return result