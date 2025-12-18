"""
QUESTION:
Create a Python function `latex_sentence` that takes a subject as input and returns a Latex formula representing the sentence "She who enjoys jogging on the seashore." Use the following Latex formula as a template: `[ exists x in text{Females} mid text{enjoys}(x, text{jogging}) land text{on}(x, text{seashore}) ]`. The function should also utilize a table of synonyms for "run" and "beach", and substitute the first synonym for each word in the formula. The table of synonyms is: `{'run': ['jog', 'sprint', 'dash'], 'beach': ['seashore', 'coast', 'shoreline']}`.
"""

SYNONYMS = {
    'run': ['jog', 'sprint', 'dash'],
    'beach': ['seashore', 'coast', 'shoreline']
}

def latex_sentence(subject):
    return f"[ exists x in text{{Females}} mid text{{enjoys}}(x, text{{{SYNONYMS['run'][0]}}}) land text{{on}}(x, text{{{SYNONYMS['beach'][0]}}}) ]"