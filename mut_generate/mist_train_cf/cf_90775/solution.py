"""
QUESTION:
Create a function named `handle_animal` that takes an animal type as a string input and returns a corresponding sound or the message "Unknown animal" if the animal type is not recognized. The function must handle at least the following animal types: "cat", "dog", "mouse", and "rabbit".
"""

def handle_animal(animal_type):
    switcher = {
        "cat": "Meow!",
        "dog": "Woof!",
        "mouse": "Squeak!",
        "rabbit": "Hop!",
    }
    
    return switcher.get(animal_type, "Unknown animal")