"""
QUESTION:
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words `"Sand"`, `"Water"`, `"Fish"`, and `"Sun"` appear without overlapping (regardless of the case).

## Examples

```python
sum_of_a_beach("WAtErSlIde")                    ==>  1
sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
sum_of_a_beach("cItYTowNcARShoW")               ==>  0
```
"""

import re

def count_beach_elements(beach):
    """
    Counts the occurrences of the words "Sand", "Water", "Fish", and "Sun" in the given string, regardless of case.

    Parameters:
    beach (str): The input string to search for the specified words.

    Returns:
    int: The total count of occurrences of the specified words.
    """
    return len(re.findall('Sand|Water|Fish|Sun', beach, re.IGNORECASE))