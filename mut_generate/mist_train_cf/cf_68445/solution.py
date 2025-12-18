"""
QUESTION:
Write a function named `decode_base64_strings` that takes a list of Base64 strings as input, where each string represents a person's information encoded in the format "Name,Age,Gender,Occupation". 

The function should decode the Base64 strings, parse the decoded strings as CSV records, and sort the records in ascending order based on the person's age. 

The function should optimize for time complexity, ideally achieving O(n log n) or better. The function should return a list of sorted records, where each record is a list of strings and integers, with the age converted to an integer for sorting.
"""

import base64
import csv
from operator import itemgetter

def decode_base64_strings(base64_strings):
    # Decode each Base64 string
    decoded_strings = [base64.b64decode(s).decode('utf-8') for s in base64_strings]
    
    # Parse each decoded string as a CSV record
    decoded_records = [list(csv.reader([s]))[0] for s in decoded_strings]
    
    # Convert age from string to int for sorting
    for record in decoded_records:
        record[1] = int(record[1])
    
    # Sort the records by age (element at index 1) in ascending order
    sorted_records = sorted(decoded_records, key=itemgetter(1))

    return sorted_records