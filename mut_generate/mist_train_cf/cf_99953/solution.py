"""
QUESTION:
Create a function `generate_narrative` that takes in the following parameters: 
- `name`: the name of the person 
- `location`: the location where the person is walking 
- `weather`: the weather condition 
- `temperature`: the temperature in Fahrenheit 
- `clothing`: a dictionary describing the person's clothing 
- `sounds`: the sounds the person hears while walking 
- `figure`: a dictionary describing the mysterious figure 
- `statue`: the description of the statue 

The function should return a string representing a third-person narrative describing the person's walk and encounter with the mysterious figure, which is actually a statue.
"""

def generate_narrative(name, location, weather, temperature, clothing, sounds, figure, statue):
    """
    Generates a third-person narrative describing a person's walk and encounter with a mysterious figure, which is actually a statue.

    Args:
    - name (str): The name of the person.
    - location (str): The location where the person is walking.
    - weather (str): The weather condition.
    - temperature (int): The temperature in Fahrenheit.
    - clothing (dict): A dictionary describing the person's clothing.
    - sounds (str): The sounds the person hears while walking.
    - figure (dict): A dictionary describing the mysterious figure.
    - statue (str): The description of the statue.

    Returns:
    - str: A string representing the third-person narrative.
    """

    narrative = f"{name} was walking in {location} on a {weather} day with a temperature of {temperature} degrees Fahrenheit. He was wearing a {clothing['shirt']} t-shirt, {clothing['shorts']} shorts, and {clothing['sneakers']} sneakers. As he walked, he could hear the sound of {sounds} and feel the cool breeze blowing through his hair.\n\n"
    narrative += f"Suddenly, he noticed a strange figure ahead of him, standing near a bench under a tree. The figure was wearing a {figure['clothing']['hoodie']} hoodie, {figure['clothing']['pants']} pants, and {figure['clothing']['boots']} boots, and was {figure['position']}. {name} hesitated for a moment but then decided to approach the figure to see if they needed any help.\n\n"
    narrative += f"As he got closer, he realized that the figure was actually a statue of a {statue}. {name} took a few pictures and continued his walk, feeling relieved and amused at the same time."

    return narrative