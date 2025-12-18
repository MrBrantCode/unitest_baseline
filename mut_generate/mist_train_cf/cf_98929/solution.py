"""
QUESTION:
Create a Python function `count_unique_patients` that takes a list of medical records, where each record is a tuple of `(patient_name, age, medication)`, and returns two lists of tuples. The first list should contain the name of each unique medication and the total number of instances it appears in the records. The second list should contain the name of each unique medication and the total number of unique patients who have been prescribed it, including those who have been prescribed different variations of that medication. The function should be able to handle a large amount of medical records.
"""

from collections import defaultdict
from itertools import groupby

def count_unique_patients(data):
    medication_dict = defaultdict(set)
    unique_patients = set()

    for patient_name, age, medication in data:
        medication_dict[medication].add(patient_name)
        unique_patients.add((patient_name, medication))

    medication_counts = [(medication, len(patients)) for medication, patients in medication_dict.items()]
    unique_patient_counts = [(medication, len(set(patient_name for patient_name, _ in patients))) 
                             for medication, patients in groupby(sorted(unique_patients, key=lambda x: x[1]), key=lambda x: x[1])]

    return medication_counts, unique_patient_counts