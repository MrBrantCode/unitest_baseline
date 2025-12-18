"""
QUESTION:
Create a function `differentiate` in the `chondroprogenitorCell` class that activates a new differentiation pathway when environmental cues contain "BMP". This pathway should set `transcriptionFactor` to "RUNX2", `signalingPathway` to "BMPR", and `epigeneticModification` to "Histone methylation". The function should also return a message indicating that the chondroprogenitor cell has differentiated into an osteoblast in the presence of BMP.
"""

def differentiate(environment):
    if "BMP" in environment:
        transcriptionFactor = "RUNX2"
        signalingPathway = "BMPR"
        epigeneticModification = "Histone methylation"
        return "Chondroprogenitor cell has differentiated into an osteoblast in the presence of BMP."