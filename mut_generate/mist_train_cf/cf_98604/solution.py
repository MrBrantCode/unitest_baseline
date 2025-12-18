"""
QUESTION:
Create a function called `suggest_substitutions` that takes in a string `ingredient` and two optional parameters `diet_restriction` and `availability`. The function should return a string suggesting a substitute for the given ingredient based on the provided `diet_restriction` and `availability`. 

The function should have access to a dictionary of rare ingredients and their corresponding substitutes. The function should return a message stating the substitute and its benefits if a suitable substitute is found, or an error message if no suitable substitute is found. 

The `diet_restriction` parameter can be one of "vegetarian", "vegan", "gluten-free", "dairy-free", or "nut-free", and the `availability` parameter can be a specific ingredient or a list of ingredients that the user has on hand.
"""

substitutions = {
    'grains of paradise': {
        'substitute': 'black pepper',
        'benefits': 'antioxidant, anti-inflammatory, anti-microbial, digestive'
    },
    'sumac': {
        'substitute': 'lemon zest',
        'benefits': 'antioxidant, anti-inflammatory, anti-bacterial, digestive'
    }
}

def suggest_substitutions(ingredient, diet_restriction=None, availability=None):
    if ingredient in substitutions:
        substitute = substitutions[ingredient]['substitute']
        benefits = substitutions[ingredient]['benefits']
        if diet_restriction:
            # Check if the substitute is suitable for the user's diet
            if diet_restriction in substitute:
                return f"You can use {substitute} as a substitute for {ingredient}. It is also {benefits}."
            else:
                return f"Sorry, there is no suitable substitute for {ingredient} that meets your dietary restrictions."
        elif availability:
            # Check if the substitute is available to the user
            if availability in substitute:
                return f"You can use {substitute} as a substitute for {ingredient}. It is also {benefits}."
            else:
                return f"Sorry, {substitute} is not available to you."
        else:
            return f"You can use {substitute} as a substitute for {ingredient}. It is also {benefits}."
    else:
        return f"Sorry, we don't have any substitution suggestions for {ingredient}."