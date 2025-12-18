"""
QUESTION:
Create a function `latex_sentence` that takes a subject of a sentence as input and returns a Latex formula depicting the sentence "[exists x in text{Females} mid text{enjoys}(x, text{action}) land text{on}(x, text{location}) ]". The function should use the given subject and the action and location should be selected from the following lists of synonyms: 
- action: 'jog', 'sprint', 'dash'
- location: 'seashore', 'coast', 'shoreline'
For a female subject, use 'Females' in the Latex formula, otherwise, use 'Males'.
"""

SYNONYMS = {
 'run': ['jog', 'sprint', 'dash'],
 'beach': ['seashore', 'coast', 'shoreline']
}

def latex_sentence(subject):
    if subject.lower() in ['he', 'him', 'his', 'himself']:
        subject_type = 'Males'
    else:
        subject_type = 'Females'

    action = SYNONYMS['run'][0]
    location = SYNONYMS['beach'][0]
    
    return f"[ exists x in text{{{subject_type}}} mid text{{enjoys}}(x, text{{{action}}}) land text{{on}}(x, text{{{location}}}) ]"