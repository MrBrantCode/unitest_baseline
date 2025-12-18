"""
QUESTION:
Write a function `find_median` that takes a string of XML data containing integer values as input, parses the XML data, and returns the median of the integers. The function should implement the Median of Medians algorithm to find the median in O(n) time complexity. The XML data is in the format `<data><value>integer</value>...</data>`.
"""

import xml.etree.ElementTree as ET

def find_median(xml_data):
    # Parse the XML data and extract the integer values
    root = ET.fromstring(xml_data)
    values = [int(value.text) for value in root.findall('value')]
    # Define a helper function to find the kth smallest element
    def kth_smallest(arr, k):
        if len(arr) == 1:
            return arr[0]
        else:
            # Divide the list into sublists of 5 elements each
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
    # Find the median of the list
    n = len(values)
    if n % 2 == 1:
        return kth_smallest(values, n//2)
    else:
        return (kth_smallest(values, n//2) + kth_smallest(values, n//2 - 1)) / 2