"""
QUESTION:
Implement the `filter_patients(patients)` function to filter a list of patient records based on specific conditions. Each patient record is a dictionary containing the keys "name", "age", "gender", and "diagnosis". The function should exclude patients if their age is less than 18, or if they are male with a diagnosis of "flu", or if they are female with a diagnosis of "migraine". The input is a list of patient records, and the output is the filtered list of patient records.
"""

def filter_patients(patients):
    return [patient for patient in patients if patient["age"] >= 18 and not ((patient["gender"] == "male" and patient["diagnosis"] == "flu") or (patient["gender"] == "female" and patient["diagnosis"] == "migraine"))]