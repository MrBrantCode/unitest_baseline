"""
QUESTION:
Implement the function `process_smiles_list(smiles_list)` that takes a list of strings, where each string is in the format "smiles|molId", and returns a dictionary where each key is a unique molecule ID and its corresponding value is the last smiles string encountered in the list.
"""

from typing import List, Dict

def process_smiles_list(smiles_list: List[str]) -> Dict[str, str]:
    smiles_dict = {}
    for entry in smiles_list:
        smiles, mol_id = entry.split("|")
        smiles_dict[mol_id] = smiles
    return smiles_dict