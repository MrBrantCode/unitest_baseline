"""
QUESTION:
Write a function named `calculate_female_average_age` that calculates the average age of female students from a given XML data string without using any external libraries. The function should have a time complexity of O(n), where n is the number of student records in the XML data, and a space complexity of O(1).
"""

def calculate_female_average_age(xml_data):
    """
    Calculate the average age of female students from a given XML data string.

    Args:
    xml_data (str): The XML data string containing student records.

    Returns:
    float: The average age of female students.
    """

    # Parse the XML data
    root = ET.fromstring(xml_data)

    total_age = 0
    female_count = 0

    # Iterate over each student element
    for student in root.iter('student'):
        # Check if the gender is female
        gender = student.find('gender').text
        if gender == 'female':
            # Add the age to the total age and increment the female count
            age = int(student.find('age').text)
            total_age += age
            female_count += 1

    # Check for division by zero
    if female_count == 0:
        return 0  # or any other default value that makes sense for your application

    # Calculate the average age of female students
    average_age = total_age / female_count

    return average_age