"""
QUESTION:
Create a Python function `latex_sentence` that generates Latex code for a sentence with a given subject who enjoys running on a beach. The function should use a list of synonyms for "run" and "beach" and return the Latex code for the sentence with the first synonym for "run" and "beach" used. The function must take the subject of the sentence as input and the Latex code should be in the format: [ exists x in text{Females} mid text{enjoys}(x, text{verb}) land text{on}(x, text{location}) ].
"""

SYNONYMS = {
 'run': ['jog', 'sprint', 'dash'],
 'beach': ['seashore', 'coast', 'shoreline']
}
def latex_sentence(subject):
 return f"[ exists x in text{{Females}} mid text{{enjoys}}(x, text{{{SYNONYMS['run'][0]}}}) land text{{on}}(x, text{{{SYNONYMS['beach'][0]}}}) ]"