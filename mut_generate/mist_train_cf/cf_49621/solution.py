"""
QUESTION:
Create a function called `compose_quatrain` that generates a quatrain with an ABAB rhyme scheme on a given theme. The function should take a string `theme` as input, where the theme is the subject of the quatrain, and return a quatrain as a string.
"""

def compose_quatrain(theme):
    if theme == 'nostalgia':
        return """In the lanes of my childhood, where memories bedew,
Echoes of old laughter, in the skies still so blue.
A carousel of dreams, spinning moments so few,
The sweet scent of innocence, how swift it outgrew."""
    else:
        # TO DO: implement more themes
        return 'Theme not supported'