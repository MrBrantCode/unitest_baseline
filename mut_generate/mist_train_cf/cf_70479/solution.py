"""
QUESTION:
Write a function `analyze_data` that takes a list of elements as input and returns a dictionary containing the total number of elements, the number of decimal numeric values, and the number of distinct typographical characters. The input list may contain a mix of float and string elements.
"""

def analyze_data(data):
    analysis = {"total_elements": 0, "decimal_values": 0, "special_characters": 0}

    for element in data:
        analysis['total_elements'] += 1

        if isinstance(element, float):
            analysis['decimal_values'] += 1
        elif isinstance(element, str):
            if not element.isalnum():
                analysis['special_characters'] += 1

    return analysis