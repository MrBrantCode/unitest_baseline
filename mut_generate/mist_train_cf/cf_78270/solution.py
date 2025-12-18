"""
QUESTION:
Create a function `generate_weekly_health_report` that takes a list of staff members' health entries as input, where each entry is a dictionary containing the staff member's ID, date, body temperature, and any health irregularities. The function should return a comprehensive weekly health report based on the recorded symptoms and entries. 

The input list should be sorted by date in ascending order. The function should group the entries by staff member ID and generate a weekly report for each staff member. The report should include a summary of daily temperature and health abnormalities (if any) highlighted. 

Assume that the input list is not empty and all entries have the required information. The report can be returned as a string or a dictionary.
"""

from datetime import datetime, timedelta
from collections import defaultdict

def generate_weekly_health_report(entries):
    """
    Generate a comprehensive weekly health report based on the recorded symptoms and entries.

    Args:
        entries (list): A list of staff members' health entries, where each entry is a dictionary containing
            the staff member's ID, date, body temperature, and any health irregularities.

    Returns:
        dict: A dictionary containing the weekly health report for each staff member.
    """
    # Sort the entries by date in ascending order
    entries.sort(key=lambda x: x['date'])

    # Group the entries by staff member ID
    staff_entries = defaultdict(list)
    for entry in entries:
        staff_entries[entry['staff_id']].append(entry)

    # Generate a weekly report for each staff member
    weekly_report = {}
    for staff_id, entries in staff_entries.items():
        report = []
        for i in range(len(entries)):
            entry = entries[i]
            date = entry['date']
            temperature = entry['temperature']
            irregularities = entry['irregularities']

            # Highlight health abnormalities (if any)
            if irregularities:
                report.append(f"{date}: Temperature - {temperature}, Health Abnormalities - {irregularities}")
            else:
                report.append(f"{date}: Temperature - {temperature}")

        weekly_report[staff_id] = report

    return weekly_report