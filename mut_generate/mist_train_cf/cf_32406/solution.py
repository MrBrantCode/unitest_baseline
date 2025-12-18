"""
QUESTION:
Create a function `extractImageName` that takes a dictionary `image` containing a "name" key with an image name and file extension as a string, and returns the image name as a string without the file extension. The function should extract the image name from the "name" key in the dictionary and remove the file extension.
"""

def extractImageName(image: dict) -> str:
    return image["name"].split(".")[0]