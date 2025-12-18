"""
QUESTION:
Create a function `convert_to_dict` that takes a list of tuples `result`, a list of column names `columns`, and a boolean `single_object`. The function should convert each tuple in `result` into a dictionary using `columns` as keys. If `single_object` is True, return the first dictionary; otherwise, return a list of dictionaries.
"""

from typing import List, Tuple, Dict, Union

def convert_to_dict(result: List[Tuple], columns: List[str], single_object: bool) -> Union[Dict, List[Dict]]:
    """Convert a list of tuples to a dict"""
    resp = [dict(zip(columns, row)) for row in result]

    if single_object:
        return resp[0]

    return resp