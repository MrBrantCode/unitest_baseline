"""
QUESTION:
Create a function `generate_diagnostic_report` that takes `patient_name`, `patient_age`, `diagnosis`, `differential_diagnosis`, and `treatment` as parameters and returns a standardized diagnostic report. The report should include the patient's name, age, the current date, the diagnosis, a list of differential diagnoses, and recommended treatments.
"""

import datetime

def generate_diagnostic_report(patient_name, patient_age, diagnosis, differential_diagnosis, treatment):
    date_today = datetime.date.today()
    report = f"""PATIENT DIAGNOSTIC REPORT

Patient Name: {patient_name}
Patient Age: {patient_age}

Date: {date_today.strftime("%B %d, %Y")}

Diagnosis: {diagnosis}

Differential Diagnoses: {', '.join(differential_diagnosis)}

Treatment: {treatment}
"""
    return report