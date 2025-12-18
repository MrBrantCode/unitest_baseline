"""
QUESTION:
Create a Python function named `latex_sentence` that takes the subject of a sentence as input and returns the LaTeX code for a formula that depicts the sentence "She who enjoys jogging on the seashore". The function must use synonyms for "run" and "beach", and the input subject must be incorporated into the LaTeX code. The function must only use the first synonym for each word.
"""

SYNONYMS = {
    'run': ['jog', 'sprint', 'dash'],
    'beach': ['seashore', 'coast', 'shoreline']
}
def latex_sentence(subject):
    return f"\\[ \\exists x \\in \\text{{{subject}}} \\mid \\text{{enjoys}}(x, \\text{{{SYNONYMS['run'][0]}}}) \\land \\text{{on}}(x, \\text{{{SYNONYMS['beach'][0]}}}) \\]"