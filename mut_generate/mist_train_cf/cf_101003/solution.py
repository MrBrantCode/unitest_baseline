"""
QUESTION:
Write a function called `generate_narrative` that generates a third-person narrative for a given scenario. The function should take a dictionary as input, where the dictionary contains the following keys: `name`, `location`, `weather`, `temperature`, `clothing` (another dictionary with keys for `shirt`, `shorts`, and `sneakers`), `sounds`, `figure` (another dictionary with keys for `clothing` and `position`), and `statue`. The function should return a string that describes the scenario in the format of a third-person narrative.
"""

def generate_narrative(scenario):
    """
    Generates a third-person narrative for a given scenario.

    Args:
        scenario (dict): A dictionary containing the scenario's details.
                         It should have the following keys:
                         - name
                         - location
                         - weather
                         - temperature
                         - clothing (another dictionary with keys for shirt, shorts, and sneakers)
                         - sounds
                         - figure (another dictionary with keys for clothing and position)
                         - statue

    Returns:
        str: A string describing the scenario in the format of a third-person narrative.
    """
    name = scenario['name']
    location = scenario['location']
    weather = scenario['weather']
    temperature = scenario['temperature']
    clothing = scenario['clothing']
    sounds = scenario['sounds']
    figure = scenario['figure']
    statue = scenario['statue']

    narrative = f"{name} was walking in {location} on a {weather} day with a temperature of {temperature} degrees Fahrenheit. He was wearing a {clothing['shirt']} t-shirt, {clothing['shorts']} shorts, and {clothing['sneakers']} sneakers. As he walked, he could hear the sound of {sounds} and feel the cool breeze blowing through his hair.\n\n"
    narrative += f"Suddenly, he noticed a strange figure ahead of him, standing near a bench under a tree. The figure was wearing a {figure['clothing']['hoodie']} hoodie, {figure['clothing']['pants']} pants, and {figure['clothing']['boots']} boots, and was {figure['position']}. {name} hesitated for a moment but then decided to approach the figure to see if they needed any help.\n\n"
    narrative += f"As he got closer, he realized that the figure was actually a statue of a {statue}. {name} took a few pictures and continued his walk, feeling relieved and amused at the same time."

    return narrative