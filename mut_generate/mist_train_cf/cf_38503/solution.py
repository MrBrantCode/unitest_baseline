"""
QUESTION:
Write a function `generate_csv_output(data: List[Dict[str, Any]], extended: bool) -> str` that takes a list of dictionaries `data` and a boolean `extended` as input. The function should generate CSV output based on the following rules:
- If `extended` is `False`, the CSV output should include only the fields `RESOLVED_ENTITY_ID`, `RELATED_ENTITY_ID`, `MATCH_LEVEL`, `MATCH_KEY`, `DATA_SOURCE`, `RECORD_ID`, and `LENS_CODE`.
- If `extended` is `True`, the CSV output should include the fields `RESOLVED_ENTITY_ID`, `RELATED_ENTITY_ID`, `MATCH_LEVEL`, `MATCH_KEY`, `DATA_SOURCE`, `RECORD_ID`, `LENS_CODE`, `REF_SCORE`, `ENTITY_TYPE`, and `ERRULE_CODE`.
The CSV output should be formatted with the fields as headers and the corresponding data for each record.
"""

from typing import List, Dict, Any

def generate_csv_output(data: List[Dict[str, Any]], extended: bool) -> str:
    if extended:
        csvFields = ['RESOLVED_ENTITY_ID', 'RELATED_ENTITY_ID', 'MATCH_LEVEL', 'MATCH_KEY', 'DATA_SOURCE', 'RECORD_ID', 'LENS_CODE', 'REF_SCORE', 'ENTITY_TYPE', 'ERRULE_CODE']
    else:
        csvFields = ['RESOLVED_ENTITY_ID', 'RELATED_ENTITY_ID', 'MATCH_LEVEL', 'MATCH_KEY', 'DATA_SOURCE', 'RECORD_ID', 'LENS_CODE']

    output = []
    output.append(','.join(csvFields))

    for record in data:
        row = [str(record.get(field, '')) for field in csvFields]
        output.append(','.join(row))

    return '\n'.join(output)