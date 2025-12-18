"""
QUESTION:
Create a function `latex_sentence` that takes the subject of the sentence as input and outputs a Latex formula depicting the sentence "She who enjoys jogging on the seashore". The formula should precisely capture the sentence's meaning and utilize synonyms for "run" and "beach" from the following lists: 'run': ['jog', 'sprint', 'dash'] and 'beach': ['seashore', 'coast', 'shoreline']. Use the first synonym for each word by default.
"""

SYNONYMS = {
    'run': ['jog', 'sprint', 'dash'],
    'beach': ['seashore', 'coast', 'shoreline']
}
def latex_sentence(subject):
    return f"\\[ \\exists x \\in \\text{{Females}} \\mid \\text{{enjoys}}(x, \\text{{{SYNONYMS['run'][0]}}}) \\land \\text{{on}}(x, \\text{{{SYNONYMS['beach'][0]}}}) \\]"