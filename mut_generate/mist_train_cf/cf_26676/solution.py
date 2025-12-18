"""
QUESTION:
Implement the `process_query_params(params, args)` function that takes in a query string `params` and a dictionary of expected parameters `args`. The function should parse the query string using `parse_qs` with `strict_parsing=True` and `keep_blank_values=True`, and then validate the parsed query parameters against the expected parameters. 

The function should check if all keys in the parsed query match the expected keys in `args`. If "p1" is present in `args`, it should be promoted to a datetime object using `types.Datetime._promote(args["p1"])` and compared with the JSON representation of the parsed query parameter "p1". 

If "p2" is present in `args` and is a float, its value in the parsed query should be "2.2". The function should return `True` if all validations pass and `False` otherwise.
"""

from urllib.parse import parse_qs
import json

def process_query_params(params, args):
    query = parse_qs(params, strict_parsing=True, keep_blank_values=True)

    # Check if all keys in query match the expected args
    if query.keys() != args.keys():
        return False

    # Promote p1 to datetime and compare with parsed query
    if "p1" in args:
        p1_graft = datetime.strptime(args["p1"], "%Y-%m-%d %H:%M:%S")
        if query["p1"] != [json.dumps(p1_graft.isoformat())]:
            return False

    # Check if p2 is a float and its value in the parsed query
    if "p2" in args and isinstance(args["p2"], float):
        if query["p2"] != ["2.2"]:
            return False

    return True