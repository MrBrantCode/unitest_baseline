"""
QUESTION:
Implement a function called `anonymize_data` that takes a list of personal data records as input and returns the anonymized records. The function should ensure that individual privacy is preserved by removing or modifying personally identifiable information. The function should also implement strong data governance policies to minimize the risk of data breaches or misuse.
"""

def anonymize_data(records):
    # Implement data anonymization logic here
    # For demonstration purposes, let's assume we're removing names and replacing them with "Anonymized"
    anonymized_records = []
    for record in records:
        anonymized_record = record.copy()
        anonymized_record['name'] = "Anonymized"
        anonymized_records.append(anonymized_record)
    return anonymized_records