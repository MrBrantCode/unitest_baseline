"""
QUESTION:
Implement a function `generate_phase_summary(default_phases)` that takes a list of default phases as input, where each default phase is a tuple of a phase template and a list of configurations for that template. The function should return a dictionary containing the phase summary, where the keys are the phase names and the values are dictionaries containing the code and inheritance information. The function should handle phase configurations with inheritance relationships.
"""

def generate_phase_summary(default_phases):
    phase_summary = {}
    for phase_template, configurations in default_phases:
        phase_name = phase_template[0] % 'S'  # Extract phase name from the template
        for parameters, code, inheritance in configurations:
            phase_summary[parameters['name']] = {'code': code, 'inheritance': inheritance}
    return phase_summary