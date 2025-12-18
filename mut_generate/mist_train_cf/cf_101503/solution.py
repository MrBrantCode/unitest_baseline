"""
QUESTION:
Create a Python function `latex_sentence` that generates LaTeX code for a formula representing the sentence "She who enjoys jogging on the seashore." The function should take the subject of the sentence as input and output the LaTeX code for the formula, utilizing a list of synonyms for "run" and "beach" to replace "jog" and "seashore" respectively. The synonyms should be stored in a dictionary with the keys "run" and "beach". The function should return a string representing the LaTeX code for the formula.
"""

SYNONYMS = {
    'run': ['jog', 'sprint', 'dash'],
    'beach': ['seashore', 'coast', 'shoreline']
}
def latex_sentence(subject):
    return f"\\[ \\exists x \\in \\text{{Females}} \\mid \\text{{enjoys}}(x, \\text{{{SYNONYMS['run'][0]}}}) \\land \\text{{on}}(x, \\text{{{SYNONYMS['beach'][0]}}}) \\]"