"""
QUESTION:
Write a function named `array_to_xml` that takes a 3x2x2 numerical array as input and returns its representation in XML format. The XML structure should have a root element containing three child "matrix" elements, each representing a 2x2 matrix in the input array. Each "matrix" element should have two child "vector" elements, representing the rows of the matrix. Each "vector" element should have two child "value" elements, representing the numbers in the row. Each element should have an "id" attribute to uniquely identify it.
"""

import xml.etree.ElementTree as ET

def array_to_xml(array):
    # create the root element
    root = ET.Element('root')
    
    # iterate over the input array
    for i, matrix in enumerate(array):
        # create a new child for each 2x2 matrix
        matrix_el = ET.SubElement(root, 'matrix', {'id': str(i+1)})
       
        # iterate over the 2x2 matrix
        for j, vector in enumerate(matrix):
            # create a new child for each vector
            vector_el = ET.SubElement(matrix_el, 'vector', {'id': str(j+1)})
            
            # iterate over vector
            for k, val in enumerate(vector):
                # create a new child for each value
                value_el = ET.SubElement(vector_el, 'value', {'id': str(k+1)})
                value_el.text = str(val)
  
    # convert the XML tree to a string
    return ET.tostring(root, encoding='utf-8').decode('utf-8')