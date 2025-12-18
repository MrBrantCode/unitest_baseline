"""
QUESTION:
Find the positions of all consonant characters in a given statement. The function, `consonant_positions`, should take a string as input and return a dictionary where the keys are the consonants found in the statement and the values are lists of positions where those consonants were found. The positions should be 0-indexed.
"""

def consonant_positions(statement):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    positions = dict()
    
    for i in range(len(statement)):
        if statement[i].lower() in consonants:
            if statement[i] in positions: 
                positions[statement[i]].append(i)
            else:
                positions[statement[i]] = [i]
                
    return positions