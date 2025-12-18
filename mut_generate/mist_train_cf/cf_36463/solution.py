"""
QUESTION:
Calculate the average score for each unique molecular fragment in a list of fragments, where each fragment is a dictionary containing a SMILES string and a score. The function `calculate_average_scores` should take a list of these fragments as input and return a dictionary mapping each unique fragment's SMILES string to its average score. The input list is of type `List[Dict[str, Union[str, float]]]` and the output dictionary is of type `Dict[str, float]`.
"""

from typing import List, Dict, Union

def entrance(molecular_fragments: List[Dict[str, Union[str, float]]]) -> Dict[str, float]:
    fragment_scores = {}
    fragment_counts = {}
    
    for fragment in molecular_fragments:
        smiles = fragment["smiles"]
        score = fragment["score"]
        
        if smiles in fragment_scores:
            fragment_scores[smiles] += score
            fragment_counts[smiles] += 1
        else:
            fragment_scores[smiles] = score
            fragment_counts[smiles] = 1
    
    average_scores = {smiles: fragment_scores[smiles] / fragment_counts[smiles] for smiles in fragment_scores}
    
    return average_scores