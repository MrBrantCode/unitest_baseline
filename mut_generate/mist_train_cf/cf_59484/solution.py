"""
QUESTION:
Write a function called `research_type` that determines the type of research based on the given characteristics. The function should take three parameters: `variable_manipulation` (boolean indicating whether any variables were manipulated), `blinding` (boolean indicating whether any form of blinding was used), and `participants_involvement` (boolean indicating whether participants were involved in the experiment). The function should return the type of research as a string.
"""

def research_type(variable_manipulation, blinding, participants_involvement):
    if variable_manipulation:
        if blinding:
            return "Experimental research with blinding"
        else:
            return "Experimental research without blinding"
    else:
        if participants_involvement:
            return "Observational research with participants"
        else:
            return "Observational research"