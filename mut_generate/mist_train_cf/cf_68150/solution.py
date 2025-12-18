"""
QUESTION:
Write a function `existComponent(component)` that checks if a given component exists in a computer system. The function should return `True` if the component exists and `False` otherwise. Note that you may not have access to the actual list of hardware components, so you can use a hypothetical list of components for demonstration purposes. The component being referred to in this context is a hardware component of a computer system capable of performing data processing and calculations, such as CPU, RAM, or Graphics Card.
"""

def existComponent(component):
    components = ['CPU', 'RAM', 'Hard Disk', 'Motherboard', 'Graphics Card']  # Hypothetical list of components
    if component in components:
        return True
    return False