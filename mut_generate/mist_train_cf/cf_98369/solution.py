"""
QUESTION:
Write a Python function `conjugate(verb)` that takes a Spanish verb as input and returns its conjugated forms in present tense. The verb is in its infinitive form, ending with 'ar', 'er', or 'ir'. The function should return the conjugated forms for all six pronouns (yo, tú, él/ella/usted, nosotros/nosotras, vosotros/vosotras, and ellos/ellas/ustedes).
"""

def conjugate(verb):
    if verb.endswith('ar'):
        stem = verb[:-2]
        endings = {
            'yo': 'o',
            'tú': 'as',
            'él/ella/usted': 'a',
            'nosotros/nosotras': 'amos',
            'vosotros/vosotras': 'áis',
            'ellos/ellas/ustedes': 'an'
        }
        return {pronoun: stem + ending for pronoun, ending in endings.items()}
    elif verb.endswith('er'):
        stem = verb[:-2]
        endings = {
            'yo': 'o',
            'tú': 'es',
            'él/ella/usted': 'e',
            'nosotros/nosotras': 'emos',
            'vosotros/vosotras': 'éis',
            'ellos/ellas/ustedes': 'en'
        }
        return {pronoun: stem + ending for pronoun, ending in endings.items()}
    elif verb.endswith('ir'):
        stem = verb[:-2]
        endings = {
            'yo': 'o',
            'tú': 'es',
            'él/ella/usted': 'e',
            'nosotros/nosotras': 'imos',
            'vosotros/vosotras': 'ís',
            'ellos/ellas/ustedes': 'en'
        }
        return {pronoun: stem + ending for pronoun, ending in endings.items()}
    else:
        return "Invalid verb"