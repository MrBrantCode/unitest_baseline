"""
QUESTION:
Write a function `find_median` that takes XML data as input and returns the median of the integers in the XML data. The XML data is in the format `<data><value>integer</value>...</data>`. The function should use the Median of Medians algorithm to find the median.
"""

import xml.etree.ElementTree as ET

def find_median(xml_data):
    root = ET.fromstring(xml_data)
    values = [int(value.text) for value in root.findall('value')]
    
    def kth_smallest(arr, k):
        if len(arr) == 1:
            return arr[0]
        else:
            sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
            medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
            pivot = kth_smallest(medians, len(medians)//2)
            left = [elem for elem in arr if elem < pivot]
            right = [elem for elem in arr if elem > pivot]
            if k < len(left):
                return kth_smallest(left, k)
            elif k < len(arr) - len(right):
                return pivot
            else:
                return kth_smallest(right, k - (len(arr) - len(right)))
                
    n = len(values)
    if n % 2 == 1:
        return kth_smallest(values, n//2)
    else:
        return (kth_smallest(values, n//2) + kth_smallest(values, n//2 - 1)) / 2