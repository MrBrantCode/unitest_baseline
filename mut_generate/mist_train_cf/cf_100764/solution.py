"""
QUESTION:
Write a function `remove_outliers` that takes an XML string as input and returns a new XML string with outliers removed from the 'grades' list. The function should use the interquartile range (IQR) method to identify outliers, specifically any values that fall outside the range of 1.5 times the IQR below the first quartile or above the third quartile. The XML structure is as follows: the root element contains a 'grades' element that has multiple 'grade' child elements with integer values.
"""

import xml.etree.ElementTree as ET
import numpy as np
def remove_outliers(xml_data):
    # Parse the XML data
    root = ET.fromstring(xml_data)
    
    # Get the grades
    grades = []
    for grade in root.findall('.//grades/grade'):
        grades.append(int(grade.text))
    
    # Calculate the IQR
    q1 = np.percentile(grades, 25)
    q3 = np.percentile(grades, 75)
    iqr = q3 - q1
    
    # Calculate the upper and lower bounds
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Remove any grades that fall outside the bounds
    new_grades = []
    for grade in grades:
        if grade >= lower_bound and grade <= upper_bound:
            new_grades.append(grade)
    
    # Update the XML data with the new grades
    for grade in root.findall('.//grades/grade'):
        if int(grade.text) not in new_grades:
            grade.getparent().remove(grade)
    
    # Return the updated XML data
    return ET.tostring(root)