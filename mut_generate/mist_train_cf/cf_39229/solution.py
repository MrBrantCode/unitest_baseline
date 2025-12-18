"""
QUESTION:
Implement the `parse` method in the `ReportParser` class to parse a report and store the extracted information in the `issued` variable. The report is a string containing multiple entries separated by double newline characters, where each entry consists of lines in the format "Key: Value". The `parse` method should take the report as input, extract the information for each entry (date, type, description), and store it in the `issued` variable as a list of dictionaries, where each dictionary represents an entry in the report.
"""

def parse(report):
    entries = report.strip().split('\n\n')  # Split the report into individual entries
    parsed_entries = []
    for entry in entries:
        lines = entry.strip().split('\n')  # Split each entry into lines
        parsed_entry = {}
        for line in lines:
            key, value = line.split(': ', 1)  # Split each line into key-value pair
            parsed_entry[key] = value
        parsed_entries.append(parsed_entry)  # Add the parsed entry to the list
    return parsed_entries  # Return the parsed entries