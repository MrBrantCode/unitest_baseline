"""
QUESTION:
Implement a function `filter_ignored_fields` that takes in a dictionary `IGNORE` and a list of data records, and returns the filtered records with specified fields ignored. The `IGNORE` dictionary contains data types as keys and lists of fields to be ignored as values. The function should iterate through the data records, check if the record type is present in the `IGNORE` dictionary, and filter out the ignored fields. If the record type is not present in the `IGNORE` dictionary, the record should be added to the filtered records as is.
"""

def filter_ignored_fields(IGNORE: dict, data_records: list) -> list:
    filtered_records = []
    for record in data_records:
        record_type = record['type']
        if record_type in IGNORE:
            ignored_fields = IGNORE[record_type]
            filtered_record = {key: value for key, value in record.items() if key not in ignored_fields}
            filtered_records.append(filtered_record)
        else:
            filtered_records.append(record)
    return filtered_records