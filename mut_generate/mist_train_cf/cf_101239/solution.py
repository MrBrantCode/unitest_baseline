"""
QUESTION:
Create a function named `count_unique_patients` that takes a list of tuples as input, where each tuple represents a medical record in the format `(patient_name, age, medication)`. The function should return two outputs: a list of tuples containing the name of each medication and the total number of instances of that medication across all patients, and a list of tuples containing the name of each medication and the total number of unique patients who have been prescribed that medication, including different variations of the medication. The function should be able to handle large datasets and count each instance of a medication only once per patient.
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