"""
QUESTION:
If you like Taco Bell, you will be familiar with their signature doritos locos taco. They're very good.


Why can't everything be a taco? We're going to attempt that here, turning every word we find into the taco bell recipe with each ingredient.


We want to input a word as a string, and return a list representing that word as a taco.

***Key***

all vowels (except 'y') = beef

t = tomato

l = lettuce

c = cheese

g = guacamole

s = salsa

  
***NOTE***    
We do not care about case here. 'S' is therefore equivalent to 's' in our taco.
  
Ignore all other letters; we don't want our taco uneccesarily clustered or else it will be too difficult to eat.

Note that no matter what ingredients are passed, our taco will always have a shell.
"""

import re

TACODICT = {
    't': 'tomato',
    'l': 'lettuce',
    'c': 'cheese',
    'g': 'guacamole',
    's': 'salsa'
}

def tacofy_word(word: str) -> list:
    """
    Converts a given word into a taco recipe list.

    Parameters:
    word (str): The input word to be converted.

    Returns:
    list: A list representing the taco recipe, starting and ending with 'shell',
          and containing ingredients based on the input word.
    """
    # Convert the word to lowercase and filter out unwanted characters
    filtered_word = re.sub('[^aeioutlcgs]+', '', word.lower())
    
    # Create the taco list with 'shell' at the beginning and end
    taco_list = ['shell'] + [TACODICT.get(c, 'beef') for c in filtered_word] + ['shell']
    
    return taco_list