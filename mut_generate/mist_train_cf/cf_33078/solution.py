"""
QUESTION:
Implement a function `process_raw_matches(raw_matches)` that takes a list of `raw_matches` as input and returns a list of dictionary objects. Each `raw_match` has attributes `external_references` and `kill_chain_phases`. The function should iterate through each `raw_match` and extract relevant information to populate the list of dictionary objects.

The dictionary objects should have the following structure:
- `score`: 1 if a `raw_match` has an external reference with `source_name` equal to 'mitre-attack' and a kill chain phase with `kill_chain_name` equal to 'mitre-attack', otherwise 0.
- `description`: derived from the `external_id` of the external reference with `source_name` equal to 'mitre-attack' in the format 'Technique <external_id> description'. 

The function should return the list of constructed dictionary objects.
"""

def process_raw_matches(raw_matches):
    technique_list = []
    for match in raw_matches:
        xid = ''
        for ref in match.external_references:
            if ref.source_name == 'mitre-attack':
                xid = ref.external_id
        score = 1 if any(phase.kill_chain_name == 'mitre-attack' for phase in match.kill_chain_phases) and xid else 0
        if score == 1:
            description = f'Technique {xid} description'
            technique_list.append({'score': score, 'description': description})
    return technique_list