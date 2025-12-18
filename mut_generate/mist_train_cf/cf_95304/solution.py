"""
QUESTION:
Write a function named `calculate_female_average_age` that takes an XML string as input, parses it, and returns the average age of the female students. The function should not use any external libraries for XML parsing and should have a time complexity of O(n), where n is the number of student records in the XML data. It should also have a space complexity of O(1), meaning that it should not use additional memory that grows with the input size.
"""

def calculate_female_average_age(xml_data):
    """
    Calculate the average age of female students from an XML string.

    Args:
        xml_data (str): The XML string containing student data.

    Returns:
        float: The average age of female students.
    """
    root = ET.fromstring(xml_data)
    total_age = 0
    female_count = 0

    for student in root.iter('student'):
        gender = student.find('gender').text
        if gender == 'female':
            age = int(student.find('age').text)
            total_age += age
            female_count += 1

    if female_count == 0:
        return 0  # or you can raise an exception
    else:
        return total_age / female_count