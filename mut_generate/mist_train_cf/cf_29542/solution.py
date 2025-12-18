"""
QUESTION:
Write a function `generate_experiment_xml` that takes four parameters: `title`, `study_accession`, `sample_accession`, and `library_name`, and returns the XML structure for the experiment in the specified format. The XML structure should have the following elements: `TITLE`, `STUDY_REF` with `accession` attribute, `DESIGN` with child elements `DESIGN_DESCRIPTION`, `SAMPLE_DESCRIPTOR` with `accession` attribute, and `LIBRARY_DESCRIPTOR` with child elements `LIBRARY_NAME` and `LIBRARY_STRATEGY`.
"""

import xml.etree.ElementTree as ET

def generate_experiment_xml(title, study_accession, sample_accession, library_name):
    experiment = ET.Element('EXPERIMENT')
    title_element = ET.SubElement(experiment, 'TITLE')
    title_element.text = title
    study_ref = ET.SubElement(experiment, 'STUDY_REF', {'accession': study_accession})
    design = ET.SubElement(experiment, 'DESIGN')
    design_description = ET.SubElement(design, 'DESIGN_DESCRIPTION')
    sample_descriptor = ET.SubElement(experiment, 'SAMPLE_DESCRIPTOR', {'accession': sample_accession})
    library_descriptor = ET.SubElement(experiment, 'LIBRARY_DESCRIPTOR')
    library_name_element = ET.SubElement(library_descriptor, 'LIBRARY_NAME')
    library_name_element.text = library_name
    library_strategy = ET.SubElement(library_descriptor, 'LIBRARY_STRATEGY')

    experiment_xml = ET.tostring(experiment, encoding='unicode')
    return experiment_xml