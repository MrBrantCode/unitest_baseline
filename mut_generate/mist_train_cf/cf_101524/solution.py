"""
QUESTION:
Create a function named `get_outfit_image` that takes a list of outfit descriptions as input, where each description is a list of strings (e.g., ["casual", "summer", "beach"]), and returns the corresponding image filename as a string (e.g., "casual_summer_beach.jpg"). The function should be able to handle any new outfit descriptions that may be added in the future. If the input outfit description does not match any known image, the function should return "Outfit image not found".
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