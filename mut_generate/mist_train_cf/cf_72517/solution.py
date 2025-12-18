"""
QUESTION:
Design a clinical trial experiment involving two groups of patients, with one group receiving medication and the other receiving a non-medication treatment (blindfolds and soft music). The patient's sleeping or awakening state is assessed through a machine recording their breathing patterns. Determine the type of blindness in this experimental design.
"""

def determine_blindness(patient_aware, assessor_aware):
    """
    Determine the type of blindness in an experimental design.

    Args:
        patient_aware (bool): Whether the patients are aware of their treatment.
        assessor_aware (bool): Whether the person assessing the treatment is aware of the treatment.

    Returns:
        str: The type of blindness in the experimental design.
    """
    if not patient_aware and not assessor_aware:
        return "Double-blind"
    elif not assessor_aware:
        return "Single-blind"
    else:
        return "Not blind"