"""
QUESTION:
Create a function `get_outfit_image(outfit_descriptions)` that takes a list of outfit descriptions as input and returns the corresponding image filename. The outfit descriptions are lists of three strings (e.g., ["casual", "summer", "beach"]), and the image filenames are strings in the format "casual_summer_beach.jpg". The function should be able to handle any new outfit descriptions that may be added in the future and return "Outfit image not found" if the input outfit description is not recognized.
"""

def get_outfit_image(outfit_descriptions):
    # Create a dictionary to map outfit descriptions to image filenames
    outfit_images = {
        "casual, summer, beach": "casual_summer_beach.jpg",
        "formal, winter, evening": "formal_winter_evening.jpg",
        "business, spring, daytime": "business_spring_daytime.jpg"
    }
    
    # Check if the input outfit description is in the dictionary
    if ", ".join(outfit_descriptions) in outfit_images:
        return outfit_images[", ".join(outfit_descriptions)]
    else:
        return "Outfit image not found"