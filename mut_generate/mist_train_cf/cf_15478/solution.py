"""
QUESTION:
Create a function named `switch_animal` that takes a string as input and returns the corresponding animal message for the given input string. The function should handle the cases: "cat", "dog", "mouse", "rabbit", "elephant", "giraffe", "lion", and "tiger". If the input string does not match any of the specified cases, the function should return a default message "The animal is not recognized."
"""

def switch_animal(animal):
    """
    This function takes a string as input and returns the corresponding animal message.

    Args:
        animal (str): The input string representing the animal.

    Returns:
        str: The corresponding animal message for the given input string.
    """
    match animal:
        case "cat":
            return "The animal is a cat."
        case "dog":
            return "The animal is a dog."
        case "mouse":
            return "The animal is a mouse."
        case "rabbit":
            return "The animal is a rabbit."
        case "elephant":
            return "The animal is an elephant."
        case "giraffe":
            return "The animal is a giraffe."
        case "lion":
            return "The animal is a lion."
        case "tiger":
            return "The animal is a tiger."
        case _:
            return "The animal is not recognized."