"""
QUESTION:
Write a function `latex_sentence` that takes a subject as input and returns a Latex formula representing the sentence "She who enjoys jogging on the seashore" with the subject incorporated. The function should use the following synonyms for "run" and "beach": 'run': ['jog', 'sprint', 'dash'], 'beach': ['seashore', 'coast', 'shoreline']. Use the first synonym for "run" and "beach" in the formula.
"""

SYNONYMS = {
 'run': ['jog', 'sprint', 'dash'],
 'beach': ['seashore', 'coast', 'shoreline']
}
def latex_sentence(subject):
 return f"[ exists x in text{{Females}} mid text{{enjoys}}(x, text{{{SYNONYMS['run'][0]}}}) land text{{on}}(x, text{{{SYNONYMS['beach'][0]}}}) ]"