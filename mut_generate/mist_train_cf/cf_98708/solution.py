"""
QUESTION:
Write a function named `modify_tense` that takes an XML string representing a sentence and a tense as input. The XML string should be in the following format:
```xml
<sentence>
    <subject>He</subject>
    <verb>is helping</verb>
    <object>his brother with the job application</object>
</sentence>
```
The function should return the modified XML string with the verb tense changed according to the input tense. The possible input tenses are 'Simple Present', 'Simple Past', and 'Present Continuous'. The modifications should be made as follows:
- Simple Present: replace "is helping" with "helps"
- Simple Past: replace "is helping" with "helped"
- Present Continuous: replace "is helping" with "is helping with"
"""

import xml.etree.ElementTree as ET

def modify_tense(xml_string, tense):
    """
    Modify the verb tense in an XML sentence.

    Args:
    xml_string (str): The input XML string representing a sentence.
    tense (str): The desired tense. Possible values are 'Simple Present', 'Simple Past', and 'Present Continuous'.

    Returns:
    str: The modified XML string with the verb tense changed.
    """
    root = ET.fromstring(xml_string)
    verb = root.find('verb').text
    if tense == 'Simple Present':
        root.find('verb').text = 'helps'
    elif tense == 'Simple Past':
        root.find('verb').text = 'helped'
    elif tense == 'Present Continuous':
        root.find('verb').text = 'is helping with'
    return ET.tostring(root, encoding='unicode')