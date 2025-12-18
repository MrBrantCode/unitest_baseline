"""
QUESTION:
Write a Python function `conjugate(verb)` that takes a Spanish verb as input and returns all its conjugated forms in present tense. The function should take into account the verb's ending to generate the correct conjugations for the following pronouns: yo, tú, él/ella/usted, nosotros/nosotras, vosotros/vosotras, and ellos/ellas/ustedes. The input verb is assumed to be in its infinitive form, ending in 'ar', 'er', or 'ir'.
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